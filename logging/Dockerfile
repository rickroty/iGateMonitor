FROM hypriot/rpi-ruby:latest  

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
     apt-utils ruby-dev gcc g++ make python-pip python-setuptools

RUN gem install fluentd --no-ri --no-doc

RUN pip install fluent-logger

RUN fluent-gem install fluent-plugin-bigquery --no-ri --no-doc

RUN apt-get remove ruby-dev gcc g++ make -y

RUN fluentd -c /etc/fluentd/fluentd.conf -p /fluentd/plugins &

ENV SSL_CERT_FILE=/etc/ca/cacert.pem/

CMD ["/bin/sh"] 
