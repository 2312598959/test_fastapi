FROM python:3.9-slim

EXPOSE 9000

WORKDIR /app


COPY ./requirements.txt /app

RUN pip3 install -r requirements.txt
COPY ./main.py /app/

ENV TZ="Asia/Shanghai"

CMD  uvicorn main:api_test --host=0.0.0.0 --port=9000
