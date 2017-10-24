#!/bin/bash
echo 'running monitor...'
docker run -v /home/pi/projects/igatemonitor:/host -e HOSTIP=$(python /home/pi/projects/igatemonitor/checkip.py) -i --rm monitoring:latest
