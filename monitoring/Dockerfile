FROM resin/rpi-raspbian:latest

RUN apt-get update -y && apt-get install -y \
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
              --no-install-recommends \
        && rm -rf /var/lib/apt/lists/*

ENV EDITOR nano

RUN git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
RUN cd Adafruit_Python_ADS1x15 && python setup.py install && pip install adafruit-ads1x15

RUN useradd ubuntu -d /home/ubuntu -m -U
RUN chown -R ubuntu:ubuntu /home/ubuntu

RUN chown -R ubuntu:ubuntu /home/ubuntu/
RUN chown -R ubuntu:ubuntu /var/run/

COPY * /home/ubuntu/
RUN chmod -R 0755 /home/ubuntu/monitor.sh
RUN rm -f /home/ubuntu/iwconfig.txt
RUN touch /home/ubuntu/iwconfig.txt
RUN chown -R ubuntu:ubuntu /home/ubuntu/iwconfig.txt

RUN mkdir -p /host
RUN chown -R ubuntu:ubuntu /host

RUN addgroup ubuntu sudo

USER ubuntu
WORKDIR /home/ubuntu

RUN pip install --user requests

# Define default command
CMD /bin/sh monitor.sh

