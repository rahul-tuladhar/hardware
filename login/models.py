from django.db import models
from django.utils import timezone


class Group(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Profile(models.Model):
    username = models.CharField(max_length=24, default='N/A')
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    display_name = models.CharField(max_length=24)
    affiliations = models.ManyToManyField(Group)

    def __str__(self):
        return self.username
