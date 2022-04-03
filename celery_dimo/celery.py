from __future__ import absolute_import, unicode_literals
from celery import Celery

from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_dimo.settings')

app = Celery('celery_dimo', backend='redis://localhost', broker='pyamqp://')

app.conf.enable_utc = False
app.conf.update(timezone='Europe/Moscow')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {

}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
