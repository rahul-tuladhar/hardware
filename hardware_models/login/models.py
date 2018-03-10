from django.db import models
from django.utils import timezone


class Group(models.Model):
    """ Attributes in alphabetical order. """
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name


class Profile(models.Model):
    """ Attributes in alphabetical order. """
    affiliations = models.ManyToManyField(Group)
    display_name = models.CharField(max_length=24)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=24, default='N/A')
    

    def __str__(self):
        return self.username
