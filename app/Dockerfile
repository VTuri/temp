FROM ubuntu:17.04
FROM selenium/standalone-chrome
FROM python:3.7.6
MAINTAINER Vajk Turi "turi.vajk@gmail.com"

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1



RUN apt update
RUN apt-get install -y libnss3 libgconf-2-4

# Install google chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

#docker build . -t doc-flask:v1
#docker run -p 5000:5000 doc-flask:v1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x /app/chromedriver

CMD flask run --host=0.0.0.0
