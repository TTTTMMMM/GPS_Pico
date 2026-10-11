from lib.my_pkg.set_ntp_time import pretty_time
from lib.my_pkg.init_routines import (
   init_UART, 
   init_display, 
   connect_to_WiFi,
   set_NTP,
   init_rotary_encoders,
   init_micro_SD,
   init_gps_module 
   )
from lib.my_pkg.konstants import seconds_between_GPS_updates
from lib.my_pkg.write_to_display import print_to_display, report
from lib.my_pkg.sd_card import (
   mount_sd_card, 
   unmount_sd_card, 
   write_latest_gps_record, 
   read_latest_gps_record
)  
import time
from lib.my_pkg.deal_with_encoder import (
   note_encoder_position, 
   execute_action,
   set_encoder_position,
   set_measurements
)
from lib.my_pkg.konstants import number_of_encoder_modes

uart = init_UART()
(display, i2c_bus) = init_display()
connected_to_WiFi_successfully = connect_to_WiFi(display, i2c_bus)        
if(connected_to_WiFi_successfully):
   set_NTP(display, i2c_bus)

(button, button_held, encoder, last_position, pixel, position) = init_rotary_encoders(i2c_bus)
sd_available = init_micro_SD(display, i2c_bus)
gps = init_gps_module(uart)

last_print = 0
taking_samples = False
while True:
   try:
      gps.update()
      latitude = gps.latitude
      longitude = gps.longitude 
   except Exception as error:
      print("\n🐘🐘🐘 GPS update error:", error)
      time.sleep(0.5)
      continue
   position =  encoder.position % number_of_encoder_modes
   if(position != last_position):
      last_position = position
      measurements = note_encoder_position(
         position, 
         pixel, 
         latitude, 
         longitude, 
         display, 
         i2c_bus
         )
   if(button.value == False):    # Button is pressed
      taking_samples = execute_action(position, display, i2c_bus)
      if (not taking_samples and position == 1):
         report(display, i2c_bus, pixel)
   now = time.monotonic()
   if ((now - last_print >= seconds_between_GPS_updates) and taking_samples):
      last_print = now
      last_position = set_encoder_position(i2c_bus, 0, pixel)
      if gps.has_fix:
         time_string = pretty_time(time.localtime())
         gps_line = f"{time_string}, ({latitude:.5f}, {longitude:.5f})\n"
         if(write_latest_gps_record(gps_line)): # Write latest GPS record to SD card
            sd_available = True
            latest_gps_record = read_latest_gps_record() # Read latest GPS record from SD card
            if latest_gps_record is not None:
               print("🦋🦋🦋 ", latest_gps_record)
               measurements = set_measurements(latitude, longitude)
               print_to_display(display, i2c_bus, 11, 1, '', '', measurements) 
         else:
            sd_available = False
            print("\n💀💀💀 Reinsert the SD card.")
            print_to_display(display, i2c_bus, 7, 1)
         if not sd_available:   # Try to remount the card after it has been reinserted.
            time.sleep(1)
            try:
               unmount_sd_card()
               time.sleep(1)
               mount_sd_card()
               sd_available = True
               print("SD card is available again")
               print_to_display(display, i2c_bus, 9, 1)
            except Exception as error:
               print("👿👿👿 SD card still unavailable:", error)
      else:
         print("Waiting for GPS fix...")
         print_to_display(display, i2c_bus, 8, 1)
   time.sleep(0.5)

