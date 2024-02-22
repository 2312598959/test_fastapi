FROM python:3.9-slim-buster

EXPOSE 9000

WORKDIR /app


COPY ./main.py /app/

ENV TZ="Asia/Shanghai"

# 声明容器启动时运行的命令
CMD ["python", "main.py"]
