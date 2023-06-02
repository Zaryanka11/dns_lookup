from django.core.management.base import BaseCommand, CommandError

from market.models import Category, Product
from bs4 import BeautifulSoup
import requests
from django.core.files import File
import shutil
from SemestrovkaCafe.settings import BASE_DIR

class Command(BaseCommand):

     def handle(self, *args, **options):
         print('Clearing DB')
         #удаляем записи и картинки
         Category.objects.all().delete()
         Product.objects.all().delete()
         try:
             shutil.rmtree('%s/media' % BASE_DIR)
         except:
             pass

         #добавляем главную страницу и парсим
         URL = 'https://terka116.ru/burgery'
         print ('Start importing from %s' %URL)
         rez = requests.get(URL, verify=False)
         soup = BeautifulSoup(rez.text, 'html.parser')

         #находим див и в нем картинки
         content = soup.find('div',{'class': 'body_20'})
         for img in content.findAll('img'):
             c = Category()
             c.name = img.get('alt')
             img_url = 'https://mosprivoz.ru/%s' % img.get('src')
             img_response = requests.get(img_url, stream=True, verify=False)
             #сохраняем временный файл
             with open('tmp.png', 'wb') as out_file:
                 shutil.copyfileobj(img_response.raw, out_file)
            #читаем временный файл
             with open('%s/tmp.png' % BASE_DIR, 'rb') as img_file:
                 c.image.save('cat.png', File(img_file), save=True)
             c.save()
             print('saving... %s' % c.name)