# TaskForge

Production-ready Task Management REST API built using Django REST Framework.

## Features

- JWT Authentication
- Task CRUD APIs
- Filtering, Search, Ordering
- Per-user task isolation
- Celery async notifications
- Redis task queue
- Swagger API documentation
- Dockerized environment
- Beautiful landing page UI

---

## Tech Stack

- Django
- Django REST Framework
- JWT Authentication
- Celery
- Redis
- Docker
- Swagger / drf-yasg

---

## API Documentation

Swagger:
`/swagger/`

ReDoc:
`/redoc/`

---

## Local Setup

```bash
pip install -r requirements/base.txt
python manage.py migrate
python manage.py runserver
```

---

## Docker Setup

```bash
docker compose up --build
```

---

## Celery Worker

```bash
celery -A TaskForge worker --loglevel=info --pool=solo
```

---

## Project Structure

```text
accounts/
tasks/
notifications/
templates/
TaskForge/
```

---

## Deployment

Render build command:

```bash
./build.sh
```

Render start command:

```bash
gunicorn TaskForge.wsgi:application
```

Required environment variables:

```text
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=.onrender.com
CELERY_BROKER_URL=redis://your-render-redis-url:6379/0
```

Optional Celery worker start command:

```bash
celery -A TaskForge worker --loglevel=info
```

---

## Author

Boddu Jagadeesh
