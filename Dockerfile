FROM python:3.12-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg wget unzip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD /bin/bash download-stt-model.sh && python playground.py
