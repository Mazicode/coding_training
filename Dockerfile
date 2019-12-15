# - coding: utf-8 --
FROM python:3.7.0 AS builder

WORKDIR /app

COPY . /app
RUN pip install --upgrade pip; \
    pip install -r requirements.txt

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8

WORKDIR /app
ADD . /api
EXPOSE 5000

ENTRYPOINT ["python3.7"]
CMD python3 flask run -h 0.0.0.0 -p 5000

