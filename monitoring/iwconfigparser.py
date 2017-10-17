import os
import sys
import time
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

for a in adapters:
    if a[:5] == "wlan0":
        wlan0=a.split("  ")

	if wlan0.count > 0:
		for reading in wlan0:
			if len(reading.translate(None, ' \n\t\r'))>0:
            			signal_strength=0
				link_quality=0
            			if reading.strip()[:6]=="Signal":
					signal_strength = reading.split("=")[1].split(" ")[0]
					#print "signal_strength:" + reading.split("=")[1].split(" ")[0]
				if reading.strip()[:4]=="Link":
					try:  link_quality = int(reading.split("=")[1].split("/")[0])*100 / int(reading.split("=")[1].split("/")[1]) 
 					except ZeroDivisionError: link_quality=0
				dt = datetime.datetime.now()
				timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
				print 'time:' + timestamp
				hostname = os.environ['HOSTIP']
				uri='http://' + hostname + ':24224'
				data='{'
				data+='\"APRS_station\": \"KG7TMT-10\",' 
				data+='"SSID": "ICU2",'
		                data+='\"signal_strength\": \"'+ str(signal_strength) +'\",'
				data+='\"link_quality\": \"'+ str(link_quality) +'\",'
		                data+='\"date\": \"'+ timestamp + '\"}'
				print "Writing stats to: " + uri
				print data
				r = requests.post(uri, json=data)
				print "response status=" + str(r.status_code)
	else:
		"wlan0 not found."

	print "done!"
	quit
