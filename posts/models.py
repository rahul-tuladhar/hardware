from django.db import models
import timezone
from login.models import User, Group

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now())
    description = models.TextField(max_length=2048)
    image = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=1.0)
    location = models.CharField(default='JPA')
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
