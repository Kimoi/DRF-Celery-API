
# DRF Celery API Project

**Implementation of asynchronous file 
processing using Celery framework**

## ✅Done:

- File model
- File Serializer
- POST /upload/
- Config Celery and Redis
- Celery async task
- Processed files status successfully changing
- GET /files/
- Environment variables
- Application is fully Dockerized
- File type validation

## ✨Give it a try:

- Clone repo
- Create `.env` file in `manage.py` directory
- Copy the code up next and fill it with your own data.
Brand new secret key is conveniently generated.
You may wipe the whole "DB" and "REDIS" section to use 
default values

```bash
SECRET_KEY=pm_rsrw&fw&(z$0j!x%n1zo$ric3-@@hbc94jv&a&dt(h_-)54
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=
DB_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=

REDIS_HOST=
REDIS_PORT=
```

- Let's spin up the container

```commandline
docker-compose up -d --build
```

- 4 containers should be running: web, db, celery, redis
```commandline
docker ps
```

- Apply migrations

```commandline
docker-compose exec web python manage.py migrate
```

- Create superuser

```commandline
docker-compose exec web python manage.py createsuperuser
```

## ⚡Example endpoints:

>>/api/upload/
> 
>POST. Allowed formats: jpeg, png, pdf, txt

>>/api/files/
>
>GET. List processed files
