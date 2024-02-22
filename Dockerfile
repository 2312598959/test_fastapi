FROM alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/python:3.11.1


EXPOSE 9000

WORKDIR /app


COPY ./main.py /app/

ENV TZ="Asia/Shanghai"

# 声明容器启动时运行的命令
CMD ["python", "main.py"]
