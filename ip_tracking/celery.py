# yourproject/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iptracking.settings')
app = Celery('iptracking')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()