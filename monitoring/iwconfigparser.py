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

output = filecontent.split("\n\n")

for l in output:
    print "["+l+"]"

print "done!"
quit
