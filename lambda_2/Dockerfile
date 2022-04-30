FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}
COPY abc2xml.py ${LAMBDA_TASK_ROOT}
COPY requester.py ${LAMBDA_TASK_ROOT}
COPY /model/ ${LAMBDA_TASK_ROOT}

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# RUN pip install -q tokenizers>=1.0.0
RUN pip install -q aitextgen --no-deps

CMD [ "app.lambda_handler" ]