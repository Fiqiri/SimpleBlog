# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /simple_blog
COPY requirements.txt /simple_blog/
RUN pip install -r requirements.txt
COPY . /simple_blog/