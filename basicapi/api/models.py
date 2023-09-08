from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    slack_name = models.CharField(max_length=32)
    current_day = models.DateField()
    utc_time = models.DateTimeField()
    track = models.CharField(max_length=32)
    github_file_url = models.URLField(max_length=200)
    github_repo_url = models.URLField(max_length=200)
    status_code = models.IntegerField(null=True)

