FROM ubuntu:xenial-20191108
ARG now
ARG commit
LABEL org.opencontainers.image.title=remote
LABEL org.opencontainers.image.authors="Alex Creek <me@alexcreek.com>"
LABEL org.opencontainers.image.source=https://github.com/alexcreek/remote
LABEL org.opencontainers.image.revision=$commit
LABEL org.opencontainers.image.created=$now

ENV LC_ALL=C.UTF-8
WORKDIR /code
EXPOSE 5000

COPY $PWD .
RUN apt update && \
  apt-get install -y curl python3 python3-pip && \
  apt-get clean && \
  pip3 install -r requirements.txt

CMD ["/usr/bin/python3", "wsgi.py"]
