from celery import shared_task
from django_celery_beat.models import PeriodicTask

from market.models import OrderProduct


@shared_task(name="repeat_order_make")
def repeat_order_make(order_id):
  order = OrderProduct.objects.get(pk=order_id)
  if order.status != '0':
    print('Статус получен!')
    task = PeriodicTask.objects.get(name='Repeat order {}'.format(order_id))
    task.enabled = False
    task.save()
  else:
    # Необходимая логика при повторной отправке заказа
    print('Я должна повторно оформлять заказ каждые 10 секунд')