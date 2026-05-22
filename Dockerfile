FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements/base.txt .

RUN pip install --upgrade pip

RUN pip install -r base.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "TaskForge.wsgi:application", "--bind", "0.0.0.0:8000"]
