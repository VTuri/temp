FROM python:3.7.6


COPY . /app
WORKDIR /app


# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt



CMD python /app/scrape.py
