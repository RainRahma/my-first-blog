from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    time_published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.time_published = timezone.now()

    