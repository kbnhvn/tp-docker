FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install requests

ADD test.py /content_test/test.py

WORKDIR /content_test/

RUN mkdir log

CMD python3 test.py