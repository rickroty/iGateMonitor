FROM resin/rpi-raspbian:latest

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y \
              gcc \
              nano \
              sudo \
              wireless-tools \
              i2c-tools \
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
              python-smbus \
              python-dev \
              python-pip \
              python-virtualenv \
              python-setuptools \
              --no-install-recommends \
        && rm -rf /var/lib/apt/lists/*

ENV EDITOR nano

RUN pip install pyserial
RUN git clone git://git.drogon.net/wiringPi
RUN cd wiringPi && ./build
RUN pip install wiringpi2

RUN echo "i2c-bcm2708" >> /etc/modules
RUN echo "i2c-dev" >> /etc/modules

RUN cd ~
RUN git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
RUN cd Adafruit_Python_ADS1x15 && python setup.py install && pip install adafruit-ads1x15

RUN useradd ubuntu -d /home/ubuntu -m -U && echo "ubuntu:ubuntu" | chpasswd && adduser ubuntu sudo
RUN echo "ubuntu ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers.d/local
RUN chown -R ubuntu:ubuntu /home/ubuntu

RUN chown -R ubuntu:ubuntu /home/ubuntu/
RUN chown -R ubuntu:ubuntu /var/run/

RUN usermod -G i2c ubuntu
#RUN chmod a+rw /dev/i2c-1

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

#CMD modprobe i2c-dev && python readvoltages.py
CMD /bin/sh monitor.sh

