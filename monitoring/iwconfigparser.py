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

try:
    c = F.read()
finally:
    F.close()

output = input.split("\n\n")

for l in output:
    print "["+l+"]"

print "done!"
quit
