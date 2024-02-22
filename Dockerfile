FROM python:3.9-slim-buster

EXPOSE 9000

WORKDIR /app


# 将当前目录下的所有文件复制到容器的工作目录中
COPY . /app

RUN pip3 install -r requirements.txt

# 设置环境变量
ENV REQUEST_ID_HEADER=x-fc-request-id

ENV TZ="Asia/Shanghai"

CMD   uvicorn main:api_test --host=0.0.0.0 --port=9000
