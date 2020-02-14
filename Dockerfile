FROM ubuntu:xenial-20191108
ENV LC_ALL=C.UTF-8
WORKDIR /code
EXPOSE 5000

RUN apt-get update && \
  apt-get install -y curl python3 python3-pip && \
  apt-get clean

COPY $PWD .
RUN pip3 install -r requirements.txt

ARG now
ARG commit
LABEL org.opencontainers.image.title=remote
LABEL org.opencontainers.image.authors="Alex Creek <me@alexcreek.com>"
LABEL org.opencontainers.image.source=https://github.com/alexcreek/remote
LABEL org.opencontainers.image.revision=$commit
LABEL org.opencontainers.image.created=$now

CMD ["/usr/bin/python3", "wsgi.py"]
