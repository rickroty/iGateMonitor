import sys
import string

try:
    input = ""
    c = sys.stdin.read(1)
    while True:
        input += c
        c = sys.stdin.read(1)
            
except EOFError:
    pass
except KeyboardInterrupt:
    pass

output = input.split("\n\n")

for l in output:
    print "["+l+"]"

sys.stdout.flush()
print "done!"
