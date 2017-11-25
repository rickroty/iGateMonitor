#!/bin/bash
#
if [ ! "$(docker ps -q -f name=monitoring)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=monitoring)" ]; then
        # cleanup
        docker rm monitoring
    fi
    docker run --name monitoring -v /home/pi/projects/igatemonitor:/host -e HOSTIP=$(python /home/pi/projects/igatemonitor/checkip.py) --network=host  --device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem --privileged  monitoring:latest
fi




