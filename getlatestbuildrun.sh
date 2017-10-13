git fetch origin
git reset --hard origin/master

docker build -t igatemonitor:v1 .

docker run -it igatemonitor:v1 
