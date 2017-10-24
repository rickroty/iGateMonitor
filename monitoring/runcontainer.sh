#!/bin/bash
cd /home/pi/projects/igatemonitor/monitoring/ && sudo rm iwconfig.txt && iwconfig > iwconfig.txt && docker run -v /home/pi/projects/igatemonitor:/host -e HOSTIP=$(python ../checkip.py) -it  monitoring:latest /bin/sh /host/monitoring/monitor.sh
