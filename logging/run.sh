if [ ! "$(docker ps -q -f name=logging)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=logging)" ]; then
        # cleanup
        docker rm logging
    fi
    docker run -d --name logging -p 24224:24224 -v /home/pi/projects/igatemonitor:/host -it logging:latest
fi


