#!/bin/bash
#
docker run -v /home/pi/projects/igatemonitor:/host -e HOSTIP=$(python /home/pi/ projects/igatemonitor/checkip.py) --network=host  --device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem --privileged -it
monitoring:latest

