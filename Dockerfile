FROM python:3.15-rc-alpine
RUN pip install celery redis flower
WORKDIR /app