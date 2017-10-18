import os
import sys
import time
import json
import string
import requests
import datetime

fname=''
filecontent=''
wlan0=[]

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    print(" No filename specified. ")
    quit

with open(fname) as f:
    filecontent = f.read()

adapters = filecontent.split("\n\n")
print "adapter count:" +str(len(adapters))
for a in adapters:
    if (a).find("wlan0")>=0:
	print "wlan0"
        wlan0=a.split("  ")
	print "wlan0 stats count:" +str(len(wlan0))
	if wlan0.count > 0:
		logit=False
            	signal_strength=0
		link_quality=0
		for reading in wlan0:
			print ">" + reading
			if len(reading.translate(None, ' \n\t\r'))>0:

            			if reading.strip()[:6]=="Signal":
					signal_strength = int(reading.split("=")[1].split(" ")[0])
					logit=True
					print "signal_strength:" + str(signal_strength)
				if reading.strip()[:4]=="Link":
					try:  link_quality = int(reading.split("=")[1].split("/")[0])*100 / int(reading.split("=")[1].split("/")[1]) 
 					except ZeroDivisionError: link_quality=0
					print "link_quality:" + str(link_quality)
					logit=True
		
		if logit:		
			epoch_time = int(time.time())
			timestamp = epoch_time
			print 'time:' + str(timestamp)
			hostname = os.environ['HOSTIP']
			uri='http://' + hostname + ':24224/wifi'
			data={"APRS_station": "KG7TMT-10", "SSID": "ICU2", "signal_strength": signal_strength, "link_quality": link_quality, "date": timestamp}
			
			print "Writing stats to: " + uri
			
			print json.dumps(data, indent=4, sort_keys=True)
			
			r = requests.post(uri, json=data)
			print "response status=" + str(r.status_code)
	else:
		"wlan0 not found."

print "done!"
quit
