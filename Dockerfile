FROM python:3.7.0 AS builder

WORKDIR /app

COPY . /app
RUN pip install --upgrade pip; \
    pip install -r requirements.txt

WORKDIR /app
ADD . /api
EXPOSE 5000
ENV FLASK_APP=api.py
ENV PYTHONIOENCODING=utf-8

ENTRYPOINT ["python3.7"]
CMD python3 -m flask run -h 0.0.0.0 -p 5000

