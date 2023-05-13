import json
import time

from celery import shared_task
import requests

from django.core.mail import send_mail
from homework.celery import app


@app.task
def send_email_task(email):
    subject = 'Random Text'
    message = generate_text()
    from_email = 'redbuzzzzzz@gmail.com'
    recipient_list = [email]
    time.sleep(50)
    send_mail(subject, message, from_email, recipient_list)


# задание = подключить апишку, чтобы отправлялся рандомный текст из апишки или погода или что нибудь еще
def generate_text():
    response = requests.get('https://evilinsult.com/')
    data = response.text
    return str(data)



@shared_task
def add(x, y):
    return x + y
