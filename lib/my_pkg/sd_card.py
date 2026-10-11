import adafruit_sdcard
import digitalio as cp_digitalio
import storage
import board
import busio

sd_mount_path = "/sd"

def mount_sd_card():
   global sd_spi, sd_cs, sd_card, sd_vfs

   sd_spi = busio.SPI(
      clock=board.GP18,
      MOSI=board.GP19,
      MISO=board.GP16
   )
   sd_cs = cp_digitalio.DigitalInOut(board.GP17)
   sd_card = adafruit_sdcard.SDCard(sd_spi, sd_cs)
   sd_vfs = storage.VfsFat(sd_card)
   storage.mount(sd_vfs, sd_mount_path)

def unmount_sd_card():
    global sd_spi, sd_cs
    try:
        storage.umount("/sd")
    except Exception:
        pass
    try:
        sd_spi.deinit()
    except Exception:
        pass
    try:
        sd_cs.deinit()
    except Exception:
        pass
    
def read_latest_gps_record():
   latest_line = None

   try:
      with open("/sd/gps_log.csv", "r") as log_file:
         for line in log_file:
               line = line.strip()

               # Ignore the header and blank lines
               if line and not line.startswith("utc_time"):
                  latest_line = line
      return latest_line
   except OSError as error:
      print("Could not read GPS log:", error)
      return None

def write_latest_gps_record(gps_line):
   try:
      with open("/sd/gps_log.csv", "a") as log_file:
         log_file.write(gps_line)
         return True
   except OSError as error:
      print("Could not write GPS log:", error)
      return False