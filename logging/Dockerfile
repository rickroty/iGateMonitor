FROM hypriot/rpi-ruby:latest  

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
     apt-utils ruby-dev gcc g++ make python-pip python-setuptools ca-certificates
    
ENV SSL_CERT_FILE=/etc/ca/GlobalSignRootCA.pem

RUN gem install fluentd --no-ri --no-doc

RUN pip install fluent-logger

RUN fluent-gem install fluent-plugin-bigquery --no-ri --no-doc

RUN apt-get remove ruby-dev gcc g++ make -y

RUN useradd pi -d /home/pi -m -U
RUN chown -R pi:pi /home/pi

USER pi
WORKDIR /home/pi

###RUN export SSL_CERT_FILE=/usr/local/etc/openssl/cert.pem

EXPOSE 24224

### docker run -it -p"24224:24224" -v "/home/pi/projects/igatemonitor/logging/:/etc/" logging:latest
CMD ["exec fluentd -c /etc/fluentd/fluentd.conf -p /fluentd/plugins"] 
