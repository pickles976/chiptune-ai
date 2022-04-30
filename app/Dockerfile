# use this for CUDA 
# FROM nvidia/cuda:11.2.0-runtime-ubuntu20.04

# RUN apt-get update && apt-get install -y software-properties-common gcc && \
#     add-apt-repository -y ppa:deadsnakes/ppa

# RUN apt-get update && apt-get install -y python3.10 python3-distutils python3-pip python3-apt

FROM python:3.10-slim

EXPOSE 5000

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./abc2xml.py ./abc2xml.py
COPY ./main.py ./main.py
COPY ./requester.py ./requester.py

COPY ./model/ ./model

RUN pip install -q aitextgen --no-deps

CMD ["python3","main.py"]