from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_author = models.CharField(max_length=100)
    post_body = models.TextField()
    post_created = models.DateTimeField(default=timezone.now)
    post_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title