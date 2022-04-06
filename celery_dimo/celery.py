from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
import os

from send_email.tasks import send_mail_func

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_dimo.settings')

app = Celery('celery_dimo', backend='redis://localhost', broker='pyamqp://')

app.conf.enable_utc = False
app.conf.update(timezone='Europe/Moscow')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    # Task name
    'send-email-everyday-at-8am': {
        'task': 'send_email.tasks.send_mail_func',
        'schedule': crontab(hour=18, minute=23),
        # this args we will pass here we can use them
        # in our function 'send_mail_func' as inputs
        # 'args': (2, )
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
