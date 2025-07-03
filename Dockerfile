FROM python:3.9-slim
WORKDIR /app
COPY file_cleanup.py .
CMD ["python", "file_cleanup.py", "--dir", "/tmp", "--days", "30"]
