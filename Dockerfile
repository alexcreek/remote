FROM python:3.7-buster
RUN unlink /etc/localtime \
  && ln -s /usr/share/zoneinfo/America/New_York /etc/localtime
WORKDIR /code
RUN pip install pipenv

ARG COMMIT
ENV FLASK_APP=remote.web FLASK_ENV=development COMMIT=${COMMIT}
COPY $PWD .
RUN python3 setup.py sdist \
  && python3 -m pip install . \
  && pipenv install --system
CMD python -u -m flask run --host 0.0.0.0 --port 8000
