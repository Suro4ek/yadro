FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./main.py ./requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]