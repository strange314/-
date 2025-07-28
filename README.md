

#  Django + FastAPI + JWT

## Django-сервис (порт 8000)
- POST `/api/gen-token/`: принимает `username`, `password` — возвращает JWT
- GET `/api/secret-data/`: защищённый эндпоинт, возвращает `{ message, user }`

## FastAPI-сервис (порт 8080)
- GET `/public-data/`: принимает JWT, пересылает в Django, если токен валиден — возвращает публичные данные

### Django
```
pip install django djangorestframework djangorestframework-simplejwt python-dotenv psycopg2
```

### FastAPI
```
pip install fastapi uvicorn httpx python-dotenv
```

## Запуск

### Django (порт 8000)
```
cd Django-сервис
python manage.py runserver
```

### FastAPI (порт 8080)
```
cd FastApi-сервис
uvicorn main:app --port 8080 --reload
```

## Пример запроса:

1. Получение токена:
```
POST http://localhost:8000/api/gen-token/
{
  "username": "admin",
  "password": "admin_password"
}
```


