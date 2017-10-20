FROM resin/rpi-raspbian:latest

RUN apt-get update -y && apt-get install -y \
              cron \
              nano \
              wireless-tools \
              autoconf \
              bison \
              build-essential \
              ca-certificates \
              curl \      
              git \
              libffi-dev \              
              libgdbm3 \
              libgdbm-dev \
              libncurses5-dev \
              libreadline6-dev \              
              libssl-dev \
              libyaml-dev \
              zlib1g-dev \ 
              python-pip \
              python-setuptools \
              rsyslog \
              --no-install-recommends \
        && rm -rf /var/lib/apt/lists/*

ENV EDITOR nano
ADD ./logentries.conf /etc/rsyslog.d/logentries.conf

# Import crontab file
ADD ./crontab /etc/crontab
RUN touch /var/log/cron.log

RUN useradd ubuntu -d /home/ubuntu -m -U
RUN chown -R ubuntu:ubuntu /home/ubuntu


RUN mkdir /home/ubuntu/monitoring
RUN chown -R ubuntu:ubuntu /home/ubuntu/monitoring
COPY * /home/ubuntu/monitoring/
RUN chmod -R 0755 /home/ubuntu/monitoring/monitor.sh


RUN mkdir -p /host
RUN chown -R ubuntu:ubuntu /host

RUN addgroup ubuntu sudo

USER ubuntu
WORKDIR /home/ubuntu


RUN pip install --user requests

### docker run -p 24224:24224 -v /home/pi/projects/igatemonitor:/host monitoring:latest
## To check if the job is scheduled
#docker exec -ti <your-container-id> bash -c "crontab -l"
## To check if the cron service is running
#docker exec -ti <your-container-id> bash -c "pgrep cron"

# Define default command
CMD rsyslogd && cron && tail -f /var/log/syslog /var/log/cron.log
