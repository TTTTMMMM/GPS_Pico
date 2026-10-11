from lib.my_pkg.konstants import server_constants
import adafruit_connection_manager
import adafruit_requests
import wifi

def check_forwarding_server() -> any:
   try:
      print(f"IPv4 Address: {wifi.radio.ipv4_address}")
      print(f"IPv4 Gateway: {wifi.radio.ipv4_gateway}")
      # url = server_constants["get_GPS_Mac"]
      url = server_constants["get_x"]
      print(f"\nChecking forwarding server at {url}")
      pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
      requests = adafruit_requests.Session(pool)
      with requests.get(url) as response:
         r = response.json()
         print(f"-->Server responded with: {r}")
   except Exception as e:
      raise Exception(f"GPS forwarding server down: {e}")   
   return (response.status_code, response.json())

def post_to_server(data: dict) -> any:
   try:
      url = server_constants["post_GPS_NAS"]  
      # url = server_constants["post_y"]  
      DATA = data
      pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
      requests = adafruit_requests.Session(pool)
      headers = {"Content-Type": "application/json"}
      with requests.post(url, json=DATA, headers=headers) as response:
         r = response.json()
         # print(f"🛀{response.json()}🛀")
   except Exception as e:
      print(f"An exception was raised in {__name__}")
      raise Exception(f"🪖 From post_to_server {e} 🪖")   
   if(response.status_code != 201):
      raise Exception(f"🪖 Status Code from forwarding server {response.status_code} \n {response.json()} 🪖")
   # return (response.status_code, response.json()['id'], response.json()['firebase_id'], response.json()['forwarder'])
   return (response.status_code)
