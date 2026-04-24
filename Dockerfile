FROM python
RUN pip install celery redis flower
WORKDIR /app