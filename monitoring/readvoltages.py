import os
import sys
import time
import json
import string
import requests
import datetime

import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()

# possible alternate bus
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# GAIN options
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

# Read  channel 2 (Battery) values into a list.
values = [0]*5
for i in range(5):
	# Read the specified ADC channel using the previously set gain value.
	value = adc.read_adc(2, gain=GAIN)
	#print value
	values[i] = value
	time.sleep(0.2)
avgvalue = sum(values)/5.00
#print avgvalue
battery_voltage = round((avgvalue/2048.00)*18.26,2)

# Read  channel 3 (Panel) values into a list.
values = [0]*5
for i in range(5):
	# Read the specified ADC channel using the previously set gain value.
	value = adc.read_adc(3, gain=GAIN)
	#print value
	values[i] = value
	time.sleep(0.2)
avgvalue = sum(values)/5.00
#print avgvalue
panel_voltage = round((avgvalue/2048.00)*18.26,2)

timestamp = int(time.time())
hostname = os.environ["HOSTIP"]
uri="http://" + hostname + ":24224/power"
data={"APRS_station": "KG7TMT-10", "battery_voltage": battery_voltage, "panel_voltage": panel_voltage, "date": timestamp}
			
print "Writing stats to: " + uri
			
print json.dumps(data, indent=4, sort_keys=True)
			
r = requests.post(uri, json=data)
print "response status=" + str(r.status_code)
