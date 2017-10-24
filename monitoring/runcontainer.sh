#!/bin/bash
cd /home/pi/projects/igatemonitor/monitoring/ && docker run -v /home/pi/projects/igatemonitor:/host -e HOSTIP=$(python /home/pi/igatemonitor/checkip.py) -i monitoring:latest /bin/sh /host/monitoring/monitor.sh
