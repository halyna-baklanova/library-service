FROM python:3.12-alpine3.20
LABEL maintainer="novabalka@gmail.com"

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install redis


COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user



# Встановлення залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання всіх файлів проєкту в контейнер
COPY . /app/

# Відкриття порту для сервера Django
EXPOSE 8000

# Команда для запуску сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

