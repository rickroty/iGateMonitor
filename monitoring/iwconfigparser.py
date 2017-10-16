import sys
import string

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
            if reading.strip()[:6]=="Signal":
                signal_strength = reading.split("=")[1].split(" ")[0]
                #print "signal_strength:" + reading.split("=")[1].split(" ")[0]
            if reading.strip()[:4]=="Link":
                link_quality = int(reading.split("=")[1].split("/")[0]) / int(reading.split("=")[1].split("/")[1]) 
                print "link_quality:" + link_quality
            #print reading.strip()    

        
        
print "done!"
quit
