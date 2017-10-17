docker run -v /home/pi/projects/igatemonitor:/host -e HOSTIP=$(python /home/pi/projects/igatemonitor/checkip.py) -it monitoring:latest
