FROM resin/rpi-raspbian:latest

RUN apt-get update -y && apt-get install -y \
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

RUN useradd ubuntu -d /home/ubuntu -m -U
RUN chown -R ubuntu:ubuntu /home/ubuntu

# for log storage (maybe shared with host)
RUN mkdir -p /fluentd/log
# configuration/plugins path (default: copied from .)
RUN mkdir -p /fluentd/etc
RUN mkdir -p /fluentd/plugins

RUN chown -R ubuntu:ubuntu /fluentd

RUN mkdir -p /host
RUN chown -R ubuntu:ubuntu /host

USER ubuntu
WORKDIR /home/ubuntu

RUN git clone https://github.com/tagomoris/xbuild.git /home/ubuntu/.xbuild
RUN /home/ubuntu/.xbuild/ruby-install 2.2.2 /home/ubuntu/ruby

ENV PATH /home/ubuntu/ruby/bin:$PATH

RUN gem install fluentd --no-ri --no-doc

RUN pip install --user fluent-logger
RUN fluent-gem install fluent-plugin-bigquery --no-ri --no-doc

# RUN gem install fluent-plugin-webhdfs

RUN curl https://raw.githubusercontent.com/rickroty/igatemonitor/master/logging/fluentd/fluentd.conf > /fluentd/etc/
#RUN cp /host/logging/fluentd/fluentd.conf /fluentd/etc

EXPOSE 24224

### docker run -p 24224 -v /home/pi/projects/igatemonitor:/host logging:latest

CMD exec fluentd -c /host/logging/fluentd/fluentd.conf
