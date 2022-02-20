FROM python:3.10-slim

EXPOSE 5000

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./abc2xml.py ./abc2xml.py
COPY ./main.py ./main.py
COPY ./requester.py ./requester.py
COPY ./keys.json ./keys.json
COPY ./request.json ./request.json

CMD ["python3","main.py"]