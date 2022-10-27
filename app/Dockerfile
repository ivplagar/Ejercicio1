FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN mkdir Characters Homer Lisa

COPY . .

CMD [ "python3", "main.py"]