import sys
import string

fname=''
filecontent=''

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    print(" No filename specified. ")
    quit

with open(fname) as f:
    filecontent = f.read()

adapters = filecontent.split("\n\n")

for a in adapters:
    if a.[:5] == "wlan0":
        wlan0=a.split("  ")

for reading in wlan0:
    print reading
print "done!"
quit
