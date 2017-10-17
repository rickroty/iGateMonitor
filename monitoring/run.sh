HOSTIP=$(python /home/pi/projects/igatemonitor/checkip.py)

docker run -v /home/pi/projects/igatemonitor:/host -e HOSTIP -it monitoring:latest
