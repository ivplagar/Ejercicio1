FROM python:latest

WORKDIR /app

COPY app/requirements.txt app/requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r app/requirements.txt
RUN mkdir app/Characters app/Homer app/Lisa

COPY . .

CMD [ "python3", "app/main.py"]