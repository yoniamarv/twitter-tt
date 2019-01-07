from django.db import models
from datetime import datetime
from profile_app.models import Profile


class Tweet(models.Model):
  text = models.TextField(max_length=140)
  date = models.DateTimeField(default=datetime.now)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

  def __str__(self):
    return self.text