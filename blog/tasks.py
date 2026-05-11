from celery import shared_task
from django.utils import timezone
from .models import Post

@shared_task
def update_blog_post_timestamp():
   current = timezone.now()
   Post.objects.all().update(last_checked=current)
