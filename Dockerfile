FROM python:3.9-slim-buster

# set work directory
WORKDIR ./src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./src/requirements.txt ./src/requirements.txt
RUN cd src/; pip install -r requirements.txt

COPY /src /src

CMD python telebot.py
