from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from sales_project import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sales_project.settings')

app = Celery('sales_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

import poll.poller

app.autodiscover_tasks()


