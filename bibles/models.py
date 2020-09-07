from django.db import models


class Bible(models.Model):

    location = models.CharField(max_length=10)
    words = models.TextField()
    description = models.TextField()
