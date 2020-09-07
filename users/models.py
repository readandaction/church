from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICES = ((GENDER_MALE, "Male"), (GENDER_FEMALE, "Female"))

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
