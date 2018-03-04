from django.db import models
from django.utils import timezone
from login.models import Profile, Group

# Create your models here.
class Post(models.Model):
	# 
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
	description = models.TextField(max_length=2048)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    location = models.CharField(default='JPA', max_length=24)
    part = models.CharField(max_length=50)1
    payment_method = models.CharField(max_length)
    price = models.FloatField(default=1.0)
    transaction_type = models.CharField(max_length=50)
    

    def __str__(self):
        return self.title
