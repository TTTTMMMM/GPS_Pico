
from lib.my_pkg.konstants import rotary_encoder_constants, seconds_between_GPS_updates
from lib.my_pkg.write_to_display import print_to_display 
from adafruit_seesaw import seesaw

def note_encoder_position(position, pixel, latitude, longitude, display, i2c_bus):
   if(position == 0):
      pixel.fill(0x00FF00)
      measurements = {
         "meaning1": "Will start taking",
         "meaning2": "samples when button",
         "meaning3": "is long pressed.",
         "meaning4": "",
         "latitude": latitude,
         "longitude": longitude
      }
      print_to_display(display, i2c_bus, 11, 1, '', '', measurements) 
   elif(position == 1):
      pixel.fill(0x0000FF)
      measurements = {
         "meaning1": "Will upload to GPS",
         "meaning2": "server over WiFi",
         "meaning3": "when button ",
         "meaning4": "is pressed.",
         "latitude": None,
         "longitude": None
      }
      print_to_display(display, i2c_bus, 11, 1, '', '', measurements) 
   elif(position == 2):
      pixel.fill(0xFF0000)
      measurements = {
         "meaning1": "Will stop taking",
         "meaning2": "samples when",
         "meaning3": "button is pressed.",
         "meaning4": "",
         "latitude": latitude,
         "longitude": longitude
      }
      print_to_display(display, i2c_bus, 11, 1, '', '', measurements) 
   return measurements

def set_measurements(latitude, longitude):
   measurements = {
      "meaning1": " Recording GPS ",
      "meaning2": " sample every",
      "meaning3": f" {seconds_between_GPS_updates} seconds.",
      "meaning4": "",
      "latitude": latitude,
      "longitude": longitude
   }
   return measurements

def set_encoder_position(i2c_bus, position, pixel):
   ss = seesaw.Seesaw(i2c_bus, rotary_encoder_constants["addresses"][0])
   ss.set_encoder_position(position)
   if(position == 0):
      pixel.fill(0x00FF00)
   elif(position == 1):
      pixel.fill(0x0000FF)
   elif(position == 2):
      pixel.fill(0xFF0000)
   return position

def execute_action(position, display, i2c_bus):
   if(position == 0):
      taking_samples = True
      return taking_samples
   elif(position == 1):
      taking_samples = False
      measurements = {
         "encoder_position": position,
         "meaning1": "",
         "meaning2": " Uploading via wifi",
         "meaning3": "",
         "meaning4": " No longer ",
         "meaning5": " recording samples.",
      }
      print_to_display(display, i2c_bus, 12, 1, '', '', measurements)
      return taking_samples
   elif(position == 2):
      print("Executing stop taking samples action.")
      taking_samples = False
      measurements = {
         "encoder_position": position,
         "meaning1": "",
         "meaning2": " Have stopped ",
         "meaning3": " recording samples.",
         "meaning4": " Turn dial to",
         "meaning5": " resume.",
      }
      print_to_display(display, i2c_bus, 12, 1, '', '', measurements)
      return taking_samples
   else:
      print("Unknown position:", position)   
      taking_samples = False
   return taking_samples

