# celery.py
from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'crypto_prices_project.settings')

app = Celery('crypto_prices_project')

app.log.setup(loglevel='DEBUG')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'update_prices_every_30_seconds': {
        'task': 'crypto_prices.tasks.update_price_list',
        'schedule': 300.0,  # Run every 30 seconds
    },
}
