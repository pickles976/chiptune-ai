# use this for CUDA 
FROM nvidia/cuda:11.6.0-runtime-ubuntu20.04

RUN apt-get update
RUN apt-get install -y software-properties-common gcc
RUN apt-get install -y python3.10 python3-distutils python3-pip python3-apt

# FROM python:3.10-slim

EXPOSE 5000

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

RUN pip install -q aitextgen --no-deps

COPY ./model/ ./model

COPY ./abc2xml.py ./abc2xml.py
COPY ./xml2abc.py ./xml2abc.py
COPY ./main.py ./main.py
COPY ./requester.py ./requester.py

CMD ["python3","main.py"]