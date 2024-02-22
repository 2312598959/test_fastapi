FROM python:3.9-slim

EXPOSE 9000

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY ./* /app
RUN pip3 install -r requirements.txt


ENV TZ="Asia/Shanghai"

CMD  uvicorn main:api_test --host=0.0.0.0 --port=9000
