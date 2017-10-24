#!/bin/bash
echo 'running monitor...'
cd /home/pi/projects/igatemonitor/monitoring/ && docker run -v /home/pi/projects/igatemonitor:/host -e HOSTIP=$(python /home/pi/projects/igatemonitor/checkip.py) -it --rm monitoring:latest
