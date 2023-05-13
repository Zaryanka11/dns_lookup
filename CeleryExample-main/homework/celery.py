import os

from celery import Celery

# Установите переменную окружения DJANGO_SETTINGS_MODULE, чтобы Celery знал, какой файл настроек Django использовать
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homework.settings')

app = Celery('homework')

# Загрузите конфигурацию Celery из файла settings.py в Django-проекте
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически загрузите задачи из всех модулей с именем tasks.py в Django-приложениях
app.autodiscover_tasks()
