import board
import busio
import displayio
from i2cdisplaybus import I2CDisplayBus
from adafruit_displayio_sh1107 import SH1107, DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297
from lib.my_pkg.sd_card import mount_sd_card
import wifi
import time
from lib.my_pkg.creds import creds_IoT
from lib.my_pkg.write_to_display import print_to_display
from lib.my_pkg.set_ntp_time import set_ntp_time_is_successful, pretty_time
from lib.my_pkg.konstants import rotary_encoder_constants
from adafruit_seesaw import  (
   seesaw, 
   rotaryio, 
   digitalio as seesaw_digitialio, 
   neopixel
)
from lib.my_pkg.sd_card import mount_sd_card, unmount_sd_card
import adafruit_gps

def init_UART():
   uart = busio.UART(
      board.GP8,          # Pico TX → GPS RX
      board.GP9,          # Pico RX ← GPS TX
      baudrate=9600, 
      timeout=10)
   return uart 

def init_display():
   displayio.release_displays() 
   # set up an I2C bus using GP27 (Yellow) as clk and GP26 (blue) as data 
   i2c_bus = busio.I2C(board.GP27, board.GP26, frequency=100000) 
   i2c_bus.unlock()
   display_bus = I2CDisplayBus(i2c_bus, device_address=0x3D)
   display = SH1107(
      display_bus,
      width=128,
      height=128,
      display_offset=DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297,
      rotation=270
   )
   return display, i2c_bus

def connect_to_WiFi(display, i2c_bus):
   try:
      print_to_display(display, i2c_bus, 1, 1)
      wifi.radio.connect(creds_IoT['ssid'], creds_IoT['password'])   # connect to wifi
      print("\n🤡🤡🤡 Wifi connected 🤡🤡🤡")
      print_to_display(display, i2c_bus, 2, 5)
      return True
   except Exception as e:
      print_to_display(display, i2c_bus, 3, 5)
      print(f"👹👹👹 Errored out trying to establish wifi:{e}\n")
      return False

def set_NTP(display, i2c_bus):
   if set_ntp_time_is_successful(wifi.radio):    # function calls ntp server to set Pico 2 W real time clock
      print_to_display(display, i2c_bus, 4, 5)
      print(f"⛑️⛑️⛑️ Set real-time clock to ntp time: {pretty_time(time.localtime())} ⛑️⛑️⛑️")
   else:
      print_to_display(display, i2c_bus, 5, 6)
      print(f"Couldn't set real-time clock to ntp time. Continuing anyway. Time is: \n{pretty_time(time.localtime())}.")

def init_rotary_encoders(i2c_bus):
   print("\n🧨🧨🧨 Initializing Rotary Encoders 🧨🧨🧨")
   # create seesaw object for rotary encoder
   seesaw_obj = seesaw.Seesaw(i2c_bus, rotary_encoder_constants["addresses"][0])
   version = (seesaw_obj.get_version() >> 16) & 0xFFFF
   if(version != 4991):
      print(f"Wrong firmware loaded for rotary encoder address 0x{rotary_encoder_constants["addresses"]:x}?  Expected 4991")

   # set up the rotary encoders a la
   # https://github.com/adafruit/Adafruit_CircuitPython_seesaw/blob/main/examples/seesaw_rotary_multiples.py
   qt_enc = seesaw.Seesaw(i2c_bus, rotary_encoder_constants["addresses"][0])
   button = seesaw_digitialio.DigitalIO(qt_enc, 24)
   button_held = False
   encoder = rotaryio.IncrementalEncoder(qt_enc)
   last_position = None
   pixel = neopixel.NeoPixel(qt_enc, 6, 1)
   pixel.brightness = .01
   pixel.fill(0x00FF00)
   position = encoder.position
   print("🧨🧨🧨 Rotary Encoders Initialized 🧨🧨🧨")
   return button, button_held, encoder, last_position, pixel, position

def init_micro_SD(display, i2c_bus):
   print("\n🐳🐳🐳 Initializing MicroSD Card 🐳🐳🐳")
   sd_available = False
   while not sd_available:
      try:
         mount_sd_card()
         try:
            with open("/sd/gps_log.csv", "r") as log_file:
               pass
         except OSError:
            with open("/sd/gps_log.csv", "w") as log_file:
               log_file.write("utc_time,latitude,longitude\n")
         sd_available = True
      except Exception as error:
         print(f"{error}")  
         unmount_sd_card()
         print_to_display(display, i2c_bus, 7, 7)
   print("🐳🐳🐳 MicroSD card initialized 🐳🐳🐳")
   return sd_available

def init_gps_module(uart):

   print("\n🦊🦊🦊 Initializing GPS module 🦊🦊🦊")
   # Create a GPS module instance
   gps = adafruit_gps.GPS(uart, debug=False)
   # Start the GPS module
   gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
   gps.send_command(b'PMTK220,1000')
   print("🦊🦊🦊 GPS module initialized 🦊🦊🦊\n")
   return gps