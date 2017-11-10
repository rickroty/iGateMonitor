FROM resin/rpi-raspbian:jessie

# Install dependencies
RUN apt-get update && apt-get install -y \
    git-core \
    build-essential \
    gcc \
    python \
    python-dev \
    python-smbus \
    python-pip \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pyserial
RUN git clone git://git.drogon.net/wiringPi
RUN cd wiringPi && ./build
RUN pip install wiringpi2

RUN cd ~
RUN git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
RUN cd Adafruit_Python_ADS1x15 && python setup.py install && pip install adafruit-ads1x15

COPY * /

# Define working directory
WORKDIR /data
VOLUME /data

CMD ["/bin/bash"]
