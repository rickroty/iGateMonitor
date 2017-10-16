git fetch origin
git reset --hard origin/master
cp /home/pi/projects/KG7TMT-10-7b0b688525e7.json /home/pi/projects/igatemonitor/logging/bigquery/

docker build -t logging:latest /home/pi/projects/igatemonitor/logging/

docker run -p 24224:24224 -v /home/pi/projects/igatemonitor:/host -it logging:latest

