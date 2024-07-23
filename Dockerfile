FROM python:3.12-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install wget unzip

RUN wget -O model https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip

COPY . .

CMD ["python", "playground.py"]


