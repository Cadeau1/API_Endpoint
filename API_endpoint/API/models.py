from django.db import models

class ApiData(models.Model):
    slack_name = models.CharField(max_length=255)
    track = models.CharField(max_length=255)
