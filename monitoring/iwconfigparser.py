import sys
import string

if len(sys.argv) &gt; 1:
    fname = sys.argv[1]
else:
    print(" No filename specified. ")
    quit

F = open(fname,”r”)

input = ""

try:
    c = F.read()
finally:
    F.close()

output = input.split("\n\n")

for l in output:
    print "["+l+"]"

print "done!"
