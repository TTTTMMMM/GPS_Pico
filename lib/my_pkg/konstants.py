ntp_constants = {
   "hours_from_GMT": -4,
   "number_of_times_to_try_calling_ntp_server": 6
}
rotary_encoder_constants = {
   "number_of_rotary_encoders": 1,
   "addresses": [0x36]
}
server_constants = {
   "get_GPS_NAS": "http://192.168.0.111:8002/gps/hello/",
   "post_GPS_NAS": "http://192.168.0.111:8002/gps/create/"
}

seconds_between_GPS_updates = 15
number_of_encoder_modes = 3