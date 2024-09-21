FROM python:3

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN mkdir /django
WORKDIR /django
COPY django/requirements.txt /django/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /django/

RUN chmod 755 django/docker/entrypoint.sh

RUN apt-get update && apt-get install -y
RUN apt-get install -y docker.io docker-compose