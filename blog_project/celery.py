from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

app = Celery('blog_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
   'update-blog-timestamps': {
      'task': 'blog.tasks.update_blog_post_timestamp',
      'schedule': crontab(),
   },
}
