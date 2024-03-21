# celery.py
from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'crypto_prices_project.settings')

app = Celery('crypto_prices_project', broker='memory://', backend='rpc://')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Configure Celery Beat schedule
app.conf.beat_schedule = {
    'update_prices_every_30_seconds': {
        'task': 'crypto_prices.tasks.update_prices',
        'schedule': 30.0,  # Run every 30 seconds
    },
}
