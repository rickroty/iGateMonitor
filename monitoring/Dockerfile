FROM resin/rpi-raspbian:latest

RUN apt-get update -y && apt-get install -y \
              cron \
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
        && rm -rf /var/lib/apt/lists/*

COPY cron /etc/cron.d/cron
chown -R ubuntu:ubuntu /var/run/
RUN crontab /etc/cron.d/cron

RUN useradd ubuntu -d /home/ubuntu -m -U
RUN chown -R ubuntu:ubuntu /home/ubuntu

# for log storage (maybe shared with host)
#RUN mkdir -p /fluentd/log
#RUN mkdir -p /fluentd/etc
#RUN mkdir -p /fluentd/plugins

#RUN chown -R ubuntu:ubuntu /fluentd

RUN mkdir -p /host
RUN chown -R ubuntu:ubuntu /host

USER ubuntu
WORKDIR /home/ubuntu

RUN pip install --user requests

### docker run -p 24224:24224 -v /home/pi/projects/igatemonitor:/host monitoring:latest
## To check if the job is scheduled
#docker exec -ti <your-container-id> bash -c "crontab -l"
## To check if the cron service is running
#docker exec -ti <your-container-id> bash -c "pgrep cron"


CMD /bin/bash
