FROM python:3.11-slim

RUN apt-get update && apt-get install -y default-jdk wget

ENV JAVA_HOME=/usr/lib/jvm/default-java

RUN pip install pyspark

WORKDIR /app

COPY . .

CMD ["spark-submit", "app.py"]