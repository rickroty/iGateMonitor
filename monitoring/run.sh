HOSTIP = `python /home/pi/projects/igatewaymonitor/checkip.py`

docker run -v /home/pi/projects/igatemonitor:/host -e HOSTIP -it monitoring:latest
