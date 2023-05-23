import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_management.settings')

app = Celery('ticket_management')

# Load tasks from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.beat_schedule = {
    'generate_employee_roster': {
        'task': 'ticket_management.employee.tasks.generate_employee_roster',
        'schedule': crontab(minute="0", hour="10"),  # every day at 10:00 AM
    },
}