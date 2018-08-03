FROM python:3

MAINTAINER richardx14 <richard@dicecentre.org>

ENV REFRESHED_AT 2018-07-30

RUN pip3 install flask flask-jsonpify flask-sqlalchemy flask-restful

ADD . /60daysofmadonna

WORKDIR /60daysofmadonna

EXPOSE 80
