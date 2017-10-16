git fetch origin
git reset --hard origin/master

docker build -t logging:latest /home/pi/projects/igatemonitor/logging/

docker run -p 24224:24224 -v /home/pi/projects/igatemonitor:/host -it logging:latest

