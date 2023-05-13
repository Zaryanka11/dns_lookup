1)pip install -r requirements.txt
2)docker-compose up
3)python manage.py runserver
4)celery -A myproject worker -l info
5)celery flower -A homework --broker=amqp://guest:guest@localhost:5672/
5)flower запускается на localhost 5555
....................................................
если отправляете письма, настройте свой smpt протокол, со своими почта/пароль