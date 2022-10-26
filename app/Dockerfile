FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN mkdir General Lisa Homer

COPY . .

CMD [ "python3", "main.py"]