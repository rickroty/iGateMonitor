if [ ! "$(docker ps -q -f name=logging:latest)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=logging:latest)" ]; then
        # cleanup
        docker rm logging:latest
    fi
    docker run -d --name logging:latest -p 24224:24224 -v /home/pi/projects/igatemonitor:/host -it logging:latest
fi


