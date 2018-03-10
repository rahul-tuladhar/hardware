from django.db import models
from django.utils import timezone
from login.models import Profile, Group

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=2048)
    image = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=1.0)
    location = models.CharField(default='JPA', max_length=24)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
