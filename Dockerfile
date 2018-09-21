FROM python:3

MAINTAINER richardx14 <richard@dicecentre.org>

ENV REFRESHED_AT 2018-08-12:1

RUN pip3 install flask flask-jsonpify flask-restful

RUN pip3 install boto3

ENV CODE_REFRESHED_AT: 2018:09:03:001

ADD . /60daysofmadonna

WORKDIR /60daysofmadonna

#EXPOSE 5002
#EXPOSE 8000

CMD ["python3", "madonna_server.py"]

#ENTRYPOINT ["/usr/bin/python3"]

# TO RUN ON DIFFERENT PORTS MODIFY THE BELOW - ADDING IN AWS CREDENTIALS IF NEEDED.  CMD IS OVERRIDDEN BY COMMAND LINE DOCKER RUN

#docker run -d -p 5010:5010 IMAGENAME python3 madonna_server.py 5010
