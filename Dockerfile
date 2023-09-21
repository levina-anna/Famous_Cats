# Используем образ Python
FROM python:3.11.5

# Устанавливаем переменную окружения для Django
ENV DJANGO_SETTINGS_MODULE=coolsite.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /Famous_Cats

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости Django
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /Famous_Cats

# Переход
WORKDIR /Famous_Cats/coolsite

# Собираем статические файлы Django
RUN python manage.py collectstatic --noinput


# Открываем порт, на котором будет работать приложение Django
EXPOSE 8000

# Запускаем Gunicorn при старте контейнера
CMD ["gunicorn", "coolsite.wsgi:application", "--bind", "0.0.0.0:8000"]

