import displayio
from adafruit_display_text import label
import terminalio
import time 
import wifi
from lib.my_pkg.set_ntp_time import pretty_time 
from lib.my_pkg.send_to_server import post_to_server

def print_to_display(display, 
                     i2c_bus, 
                     block_number: int, 
                     delay_in_secs: int, 
                     id: str="-",
                     fb_id: str='',
                     measurements: dict={}) -> None:
   display_lines = ["-" for _ in range(10)]
   if(block_number==1):
      display_lines[0] = f"Connecting to Wifi"
      write_to_display(display, display_lines)
   elif(block_number==2):
      display_lines[0] = "Connected to Wifi"
      display_lines[1] = f"IP: {wifi.radio.ipv4_address}"
      display_lines[2] = "Setting RTC clock"
      write_to_display(display, display_lines)
   elif(block_number==3):
      display_lines[1] = "Could not "
      display_lines[2] = "connect to"
      display_lines[3] = "wifi"
      display_lines[4] = ""
      write_to_display(display, display_lines)
   elif(block_number==4):
      time_string = pretty_time(time.localtime())
      display_lines[0] = "Connected to Wifi"
      display_lines[1] = "Set RTC clock to"
      display_lines[2] = f"{time_string[:-3]}"
      write_to_display(display, display_lines)
   elif(block_number==5):
      time_string = pretty_time(time.localtime())
      display_lines[0] = f"{time_string[:-3]}"
      display_lines[1] = "Could not"
      display_lines[2] = "set real-time"
      display_lines[3] = "clock"
      write_to_display(display, display_lines)
   elif(block_number==6):
      time_string = pretty_time(time.localtime())
      display_lines[0] = f"{time_string[:-3]}"
      display_lines[1] = f"IP: {wifi.radio.ipv4_address}"
      write_to_display(display, display_lines)
   elif(block_number==7):
      time_string = pretty_time(time.localtime())
      display_lines[0] = f"{time_string[:-3]}"
      display_lines[1] = " "
      display_lines[2] = "Could not write to"
      display_lines[3] = "the SD card..."
      display_lines[4] = "Check that it is"
      display_lines[5] = "properly inserted."
      display_lines[6] = "Then wait for"
      display_lines[7] = "next GPS sample."
      display_lines[8] = " "
      write_to_display(display, display_lines)
   elif(block_number==8):
      time_string = pretty_time(time.localtime())
      display_lines[0] = f"{time_string[:-3]}"
      display_lines[1] = ""
      display_lines[2] = "Waiting for GPS fix..."
      display_lines[3] = ""
      write_to_display(display, display_lines)
   elif(block_number==9):
      time_string = pretty_time(time.localtime())
      display_lines[0] = f"{time_string}"
      display_lines[1] = ""
      display_lines[2] = "SD card is available"
      display_lines[3] = "again!"
      display_lines[4] = "Awaiting next reading"
      write_to_display(display, display_lines)
   elif(block_number==10):
      time_string = pretty_time(time.localtime())
      display_lines[0] = f"{time_string}"
      display_lines[1] = ""
      display_lines[2] = "Failed to mount SD."
      display_lines[3] = "Insert an SD card"
      display_lines[4] = "and hold tight."
      write_to_display(display, display_lines)
   elif(block_number==11):
      time_string = pretty_time(time.localtime())
      latitude = measurements["latitude"]
      longitude = measurements["longitude"]
      meaning1 = measurements["meaning1"]
      meaning2 = measurements["meaning2"]
      meaning3 = measurements["meaning3"] 
      meaning4 = measurements["meaning4"] 
      display_lines[0] = f"{time_string}"
      display_lines[1] = f"Lat: {latitude:.5f}" if latitude is not None else " "
      display_lines[2] = f"Lat: {longitude:.5f}" if longitude is not None else " "
      display_lines[3] = ""
      display_lines[4] = f"{meaning1}"
      display_lines[5] = f"{meaning2}"
      display_lines[6] = f"{meaning3}"
      display_lines[7] = f"{meaning4}"
      display_lines[8] = ""
      write_to_display(display, display_lines)
      time_string = pretty_time(time.localtime())
   elif(block_number==12):
      time_string = pretty_time(time.localtime())
      meaning1 = measurements["meaning1"]
      meaning2 = measurements["meaning2"]
      meaning3 = measurements["meaning3"] 
      meaning4 = measurements["meaning4"] 
      meaning5 = measurements["meaning5"] 
      display_lines[0] = f"{time_string}"
      display_lines[1] = ""
      display_lines[2] = f"{meaning1}"
      display_lines[3] = f"{meaning2}"
      display_lines[4] = f"{meaning3}"
      display_lines[5] = f"{meaning4}"
      display_lines[6] = f"{meaning5}"
      display_lines[7] = ""
      display_lines[8] = ""
      write_to_display(display, display_lines)
      time_string = pretty_time(time.localtime())
   elif(block_number==13):
      time_string = pretty_time(time.localtime())
      meaning1 = measurements["meaning1"]
      meaning2 = measurements["meaning2"]
      meaning3 = measurements["meaning3"] 
      meaning4 = measurements["meaning4"] 
      meaning5 = measurements["meaning5"] 
      meaning6 = measurements["meaning6"] 
      display_lines[0] = f"{time_string}"
      display_lines[1] = ""
      display_lines[2] = f"{meaning1}"
      display_lines[3] = f"{meaning2}"
      display_lines[4] = ""
      display_lines[5] = f"{meaning3}"
      display_lines[6] = f"{meaning4}"
      display_lines[7] = f"{meaning5}"
      display_lines[8] = f"{meaning6}"
      write_to_display(display, display_lines)
      time_string = pretty_time(time.localtime())
   elif(block_number==14):
      time_string = pretty_time(time.localtime())
      meaning1 = measurements["meaning1"]
      meaning2 = measurements["meaning2"]
      meaning3 = measurements["meaning3"] 
      meaning4 = measurements["meaning4"] 
      meaning5 = measurements["meaning5"] 
      display_lines[0] = f"{time_string}"
      display_lines[1] = ""
      display_lines[2] = f"{meaning1}"
      display_lines[3] = f"{meaning2}"
      display_lines[4] = f"{meaning3}"
      display_lines[5] = ""
      display_lines[6] = f"{meaning4}"
      display_lines[7] = f"{meaning5}"
      display_lines[8] = ""
      write_to_display(display, display_lines)
      time_string = pretty_time(time.localtime())
   else:
      time_string = pretty_time(time.localtime())
      display_lines[0] = f"{time_string}"
      display_lines[1] = f"Wrong block"
      display_lines[2] = f"number param"
      display_lines[3] = f"in print"
      write_to_display(display, display_lines)
   time.sleep(delay_in_secs)
   return None

def write_to_display(display, text_list: list) -> None:
   # Make the display context
   BORDER = 2
   Y_DELTA = 13
   Y_INIT = 6
   splash = displayio.Group()
   display.root_group = splash

   color_bitmap = displayio.Bitmap(128, 128, 1)
   color_palette = displayio.Palette(1)
   color_palette[0] = 0xFFFFFF  # White
   bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
   splash.append(bg_sprite)

   # Draw a smaller inner rectangle in black
   inner_bitmap = displayio.Bitmap(128 - BORDER * 2, 128 - BORDER * 2, 1)
   inner_palette = displayio.Palette(1)
   inner_palette[0] = 0x000000  # Black
   inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
   splash.append(inner_sprite)

   font = terminalio.FONT
   text_area = label.Label(font, text=text_list[0], x=3 + BORDER, y=Y_INIT + BORDER)
   splash.append(text_area)
   text_area = label.Label(font, text=text_list[1], x=3 + BORDER, y=Y_INIT + BORDER + Y_DELTA*1)
   splash.append(text_area)
   text_area = label.Label(font, text=text_list[2], x=3 + BORDER, y=Y_INIT + BORDER + Y_DELTA*2)
   splash.append(text_area)
   text_area = label.Label(font, text=text_list[3], x=3 + BORDER, y=Y_INIT + BORDER + Y_DELTA*3)
   splash.append(text_area)   
   text_area = label.Label(font, text=text_list[4], x=3 + BORDER, y=Y_INIT + BORDER + Y_DELTA*4)
   splash.append(text_area)   
   text_area = label.Label(font, text=text_list[5], x=3 + BORDER, y=Y_INIT + BORDER + Y_DELTA*5)
   splash.append(text_area)   
   text_area = label.Label(font, text=text_list[6], x=3 + BORDER, y=Y_INIT + BORDER + Y_DELTA*6)
   splash.append(text_area) 
   text_area = label.Label(font, text=text_list[7], x=3 + BORDER, y=Y_INIT + BORDER + Y_DELTA*7)
   splash.append(text_area) 
   text_area = label.Label(font, text=text_list[8], x=3 + BORDER, y=Y_INIT + BORDER + Y_DELTA*8)
   splash.append(text_area) 
   # text_area = label.Label(terminalio.FONT, text=text_list[9], x=3 + BORDER, y=113 + BORDER)
   # splash.append(text_area)
   return None


def report(display: any = {}, i2c_bus: any = {}, pixel: any = None) -> None:
   records = []
   try:
      with open("/sd/gps_log.csv", "r") as log_file:
         log_lines = log_file.readlines()
   except OSError as error:
      print(f"💀 Could not read GPS log: {error} 💀")
      return None

   print(f"Number of GPS records on SD card: {len(log_lines)}")
   retained_lines = []
   invalid_record_found = False
   record_count = 0
   for raw_line in log_lines:
      line = raw_line.strip()
      if not line or line.startswith("utc_time"):
         retained_lines.append(raw_line)
         continue
      record_count += 1
      try:
         timestamp, coordinates = line.split(",", 1)
         date_part, time_part = timestamp.strip().split(" ", 1)
         year, month_name, day = date_part.split("-")
         month = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split().index(month_name) + 1
         iso_timestamp = f"{year}-{month:02d}-{int(day):02d}T{time_part}"
         latitude, longitude = coordinates.strip().strip("() ").split(",", 1)
         measurements = {
            "dt": iso_timestamp,
            "lat": float(latitude.strip()),
            "lon": float(longitude.strip())
         }
         records.append((measurements, raw_line))
         retained_lines.append(raw_line)
      except ValueError as error:
         invalid_record_found = True
         print(f"💀 Could not parse record: {error} 💀")

   if invalid_record_found:
      print("Invalid records found and removed.")
      try:
         with open("/sd/gps_log.csv", "w") as log_file:
            for retained_line in retained_lines:
               log_file.write(retained_line)
      except OSError as error:
         print(f"💀 Could not remove invalid GPS records: {error} 💀")

   measurements = {}
   error_count = 0
   for index, (measurements, source_line) in enumerate(records):
      if index > 0:
         time.sleep(1)
      try:
         response_code = post_to_server(measurements)
         if response_code == 201:
            if pixel is not None:
               pixel.fill(0x00FF00)
               time.sleep(0.25)
               pixel.fill(0x0000FF)
            try:
               with open("/sd/gps_log.csv", "r") as log_file:
                  current_lines = log_file.readlines()
               removed = False
               with open("/sd/gps_log.csv", "w") as log_file:
                  for current_line in current_lines:
                     if not removed and current_line == source_line:
                        removed = True
                        continue
                     log_file.write(current_line)
               if not removed:
                  print(f"Could not find posted record {index + 1} in the SD log.")
            except OSError as error:
               error
               print(f"Posted record {index + 1}, but could not remove it from the SD log: {error}")
      except Exception as error:
         error_count += 1
         print(f"Could not post record {index + 1}: {error}")
         measurements["meaning1"] = f"Could not post"
         measurements["meaning2"] = f"record {index + 1}. "
         measurements["meaning3"] = f"Server error"
         measurements["meaning4"] = ""
         measurements["meaning5"] = f"Talk to management"
         print_to_display(display, i2c_bus, 14, 1, measurements=measurements)
   if error_count == 0:
      try:
         measurements["meaning1"] = f"{index + 1} records"
      except Exception as error:
         measurements["meaning1"] = " 0 records"
      measurements["meaning2"] = " posted"
      measurements["meaning3"] = ""
      measurements["meaning4"] = "Turn knob"
      measurements["meaning5"] = "to first position"
      measurements["meaning6"] = "to collect GPS data"
      print_to_display(display, i2c_bus, 13, 1, measurements=measurements)
   return None

