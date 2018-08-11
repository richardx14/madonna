FROM python:3

MAINTAINER richardx14 <richard@dicecentre.org>

ENV REFRESHED_AT 2018-08-11:2

RUN pip3 install flask flask-jsonpify flask-sqlalchemy flask-restful

RUN pip3 install boto3

ENV CODE_REFRESHED_AT: 2018:08:11:8

ADD . /60daysofmadonna

WORKDIR /60daysofmadonna

#EXPOSE 5002
#EXPOSE 8000

CMD ["python3", "madonna_server.py"]
