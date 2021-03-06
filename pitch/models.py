from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    pitch_title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pitch_title
