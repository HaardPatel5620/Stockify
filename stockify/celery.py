from __future__ import absolute_import,unicode_literals
import os 

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockify.settings')

app = Celery('stockify')

app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/kolkata')

app.config_from_object(settings, namespace='CELERY')

# celery beat settings

app.conf.beat_schedule = {
    # 'every-10-seconds' :{
    #     'task':'app.tasks.update_stock',
    #     'schedule': 10,
    #     'args': ([['RELIANCE.NS','BAJAJFINSV.NS']])
    # }
}

# Load task modules from all registered Django apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')