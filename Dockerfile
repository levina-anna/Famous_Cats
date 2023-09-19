# Используем образ Python
FROM python:3.11.5

# Устанавливаем переменную окружения для Django
ENV DJANGO_SETTINGS_MODULE=gvksite.settings

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /gvk

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости Django
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . . /gvk

# Переход
WORKDIR /gvk/gvksite

# Открываем порт, на котором будет работать приложение Django
EXPOSE 8000

# Запускаем приложение при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
