FROM python:3.11.5

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITTEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Обновляем pip
RUN pip install --upgrade pip

# Устанавливам необходимые зависимости для работы программы
RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext \
     cron openssh-client flake8 locales vim

# Создаем пользователя
RUN useradd -rms /bin/bash yt && chmod 777 /opt /run

# Создаем текущий рабочий каталог внутри контейнера
WORKDIR /yt

# Создаем директории для static и media (для volume)
RUN mkdir /yt/static && mkdir /yt/media && chown -R yt:yt /yt && chmod 755 /yt