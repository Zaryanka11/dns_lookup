import json

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from market.models import OrderProduct

class Command(BaseCommand):
  def add_arguments(self, parser):
    parser.add_argument('status', type=str)
    parser.add_argument('order_id', nargs=1, type=int)

  def handle(self, *args, **options):
    status = options['status']
    order = OrderProduct.objects.get(pk=options['order_id'][0])
    if status == '0':
      PeriodicTask.objects.create(
          name='Repeat order {}'.format(options['order_id']),
          task='repeat_order_make',
          interval=IntervalSchedule.objects.get(every=10, period='seconds'),
          args=json.dumps([options['order_id'][0]]),
          start_time=timezone.now(),
        )
    else:
      order.update(status=status)
      order.refresh_from_db()
      # Необходимая логика после удачного получения статуса
      print('Статус вашего заказа -> {}'.format(order.status))