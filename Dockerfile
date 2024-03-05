FROM python:3.9-slim-buster
EXPOSE 9000

WORKDIR /app



COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt

COPY ./static /app/static
COPY ./src /app/src
COPY ./app.py /app/app.py

ENV TZ="Asia/Shanghai"

CMD uvicorn app:api --host=0.0.0.0 --port=9000
