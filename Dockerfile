FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
# install req for python modules using gcc
RUN apk add python3-dev build-base --update-cache
RUN apk add make libffi-dev openssl-dev nodejs
RUN npm install -g bower

ADD . /code/
RUN pip install -r requirements.txt
RUN python3 manage.py migrate

WORKDIR /code/todo/static/
RUN bower install --allow-root

