FROM python:3.8 as host

RUN apt-get update -qq && apt-get install vim -qqq

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

ADD . .

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
