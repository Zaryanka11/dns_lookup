# Используем готовый Docker - образ, который включается в себя версию питона 3.9
FROM python:3.9-alpine
# указываем директорию, что мы находимся в корне проекта
WORKDIR .
# используем переменное окружение
ENV DJANGO_SETTINGS_MODULE=docx_linter.settings
ENV PYTHONUNBUFFERED=1

# установлены зависимости для postgresql
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# установить и обновить зависимости нашего приложения
RUN pip install --upgrade pip

# перенос образа из нашей системы в Linux
# что скопировать и по какому пути (в корень проекта)
COPY ./req.txt .
# устанавливаем зависимости нашегo приложения из файла (параметр -r)
RUN pip install -r req.txt

# копируем всё наше приложение
COPY . .