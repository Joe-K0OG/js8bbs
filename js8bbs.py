#!/usr/bin/env python3
# coding: utf-8

import sys
import time
import json
from js8net import *
import re
import requests
import os
import os.path
import settings

# Original JS8Help By Paul VandenBosch - KC8WBK
# Modified - K0OG - 6/27/2022

#####  User Configurable Parameters  #####
#   Settings are read from settings.py   #

# Check how many executable datasets of 
#   triggers/exefiles/outfiles to import.
# Open and read the settings file
file = open("settings.py", "r")
# Read content of the settings file
data = file.read()
# Count how many trigger datasets are in the settings file
datasets = data.count("trigger_")
print('\n*** Number of executable Datasets = ',datasets)
# Scan the settings file for trigger/exe/output sets
print("\n*** Trigger / Executable / Output ***")
print('---------------------------------------------------')
for n in range(1,datasets+1):
 exec('trigger' + str(n) + ' = ' + 'settings.trigger_' + str(n))
 exec('exefile' + str(n) + ' = ' + 'settings.exefile_' + str(n))
 exec('outfile' + str(n) + ' = ' + 'settings.outfile_' + str(n))
 
 print('T =', eval('trigger' + str(n)).upper(), '\nE =', eval('exefile' + str(n)), '\nO =', eval('outfile' + str(n)))
 print('---------------------------------------------------')

js8host="localhost"
js8port=2442

print("\n*** Configuration Parameters loaded ***\n")

##### End of configuration #####

# Clean out old rx.json file to keep it from becoming bloated
os.system('cat /dev/null > rx.json')

print("Connecting to JS8Call...")
start_net(js8host,js8port)
print("Connected to",js8host,':',js8port)
get_band_activity()
my_call = get_callsign()
print(my_call + ' JS8Call BBS Station Active...')
print()

last=time.time()
while(True):
    time.sleep(0.1)
    if(not(rx_queue.empty())):
        with rx_lock:
            rx=rx_queue.get()
            f=open("rx.json","a")
            f.write(json.dumps(rx))
            f.write("\n")
            f.close()
# Check for a message directed to my callsign    
            if(rx['type']=="RX.DIRECTED" and my_call == rx['params']['TO']):
                directed_message_to_my_call = rx['params']['TEXT']
# Split the recieved directed message
                split_message = re.split('\s', directed_message_to_my_call)
# Search for trigger...
# Only implement trigger if it is the first word in the input stream
# after the callsigns, which is at word position 3.
#
                for d in range(1,datasets+1):
                      trigger = eval("trigger" + str(d)).upper()
                      if split_message[3] == trigger:
                         request_call_raw = split_message[0]
                         request_call = request_call_raw.strip(':')
                         os.system(eval("exefile" + str(d)))
                         if os.path.exists(eval("outfile" + str(d))):
                           report_file = open(eval("outfile" + str(d)))
                           report_msg = report_file.read()
                           print(request_call + ' CMD COMPLETE\n' + report_msg)
                           send_inbox_message(request_call, report_msg)
                           report_file.close()
                         else:
                              send_directed_message(request_call, 'CMD COMPLETE')
