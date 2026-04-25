# Базовый образ: Python 3.11 на Alpine Linux (минимальный и лёгкий дистрибутив)
FROM python:3.11-alpine3.17

# Установка системных зависимостей
RUN apk add --no-cache \
    curl \
    bash \
    build-base \
    libffi-dev \
    openssl-dev \
    openjdk11-jre \
    tar \
    wget

# Версия Poetry (менеджер зависимостей Python)
ENV POETRY_VERSION=2.3.4

# Директория установки Poetry
ENV POETRY_HOME=/opt/poetry

# Добавление Poetry и user-local bin в PATH,
# чтобы команда `poetry` была доступна глобально
ENV PATH="$POETRY_HOME/bin:/root/.local/bin:$PATH"

# Установка Poetry через официальный install-скрипт
# (ставится в POETRY_HOME)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Отключаем создание виртуальных окружений Poetry,
# чтобы зависимости ставились прямо в системный Python контейнера
RUN poetry config virtualenvs.create false

# Рабочая директория внутри контейнера
WORKDIR /usr/workspace

# Копируем только файлы зависимостей сначала
# (это позволяет кешировать слой Docker и не переустанавливать зависимости при изменении кода)
COPY pyproject.toml poetry.lock ./

# Установка Python-зависимостей через Poetry
# --no-interaction: без интерактивного режима
# --no-ansi: отключение цветного вывода (чище логи)
RUN poetry install --no-interaction --no-ansi

# Копируем весь исходный код проекта в контейнер
COPY . .

# Установка Allure (инструмент для отчетов тестирования):
# - скачиваем архив с Maven репозитория
# - распаковываем в /opt
# - создаём символическую ссылку для удобного запуска команды `allure`
RUN curl -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.32.0/allure-commandline-2.32.0.tgz \
    | tar -xz -C /opt/ \
    && ln -s /opt/allure-2.32.0/bin/allure /usr/local/bin/allure
