# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

# print to logs
ENV PYTHONUNBUFFERED=True

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 

# copy everything after tests to speed up caching
COPY . .

# install the notification-agent with pip
RUN pip install -e .

CMD python air_gradient_agent