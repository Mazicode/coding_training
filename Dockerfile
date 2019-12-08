FROM python:3.7.0-alpine AS builder

COPY requirements.txt /

WORKDIR /app

RUN RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
ENV FLASK_APP=app.py
CMD flask run -h 0.0.0.0 -p 5000

CMD [ "python", "./app" ]