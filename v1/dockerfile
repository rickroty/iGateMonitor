FROM hypriot/rpi-ruby:latest  
ENTRYPOINT []

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
  curl

RUN gem install fluentd
RUN apt-get install -qy python-setuptools
RUN easy_install pip

CMD ["/bin/sh"] 
