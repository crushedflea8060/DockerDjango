from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.user.username}" 
class Post(models.Model):
   title = models.CharField(max_length=200)
   author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
   body = models.TextField()
   last_checked = models.DateTimeField(default=timezone.now)
   def get_meta(self):
      return{
      "id" : self.id,
      "title" : self.title,
      "author" : self.author.username,
      "last_checked" : self.last_checked,
      "url" : self.get_absolute_url()
      }
 
   def __str__(self):
      return self.title
   def get_absolute_url(self):
      return reverse('post_detail', args=[str(self.id)])
