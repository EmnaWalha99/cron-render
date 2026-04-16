FROM  python:3.11

WORKDIR /app
COPY app /app
CMD ["python", "task.py"]