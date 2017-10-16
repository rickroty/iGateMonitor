import sys
import string

fname=''
content=''

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    print(" No filename specified. ")
    quit

with open(fname) as f:
    content = f.read()

output = input.split("\n\n")

for l in output:
    print "["+l+"]"

print "done!"
quit
