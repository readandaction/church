from django.db import models


class Havior(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(blank=True)
    bibles = models.ManyToManyField("bibles.Bible", related_name="haviors")
    user = models.ForeignKey("users.User", related_name="haviors")
