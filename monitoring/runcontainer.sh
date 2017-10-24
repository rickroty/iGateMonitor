#!/bin/bash
cd /home/pi/projects/igatemonitor/monitoring/ && docker run -v /home/pi/projects/igatemonitor:/host -e HOSTIP=$(python /home/pi/projects/igatemonitor/checkip.py) -i --rm monitoring:latest /bin/sh cd /host/monitoring/ && /bin/sh monitor.sh
