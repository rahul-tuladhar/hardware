from django.db import models
from django.utils import timezone
from login.models import Profile, Group

# Create your models here.
class Post(models.Model):
	# Alphabetical order
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now)
	description = models.TextField(max_length=2048)
	image = models.ImageField(blank=True, null=True)
	location = models.CharField(default='JPA', max_length=24)
	part = models.CharField( default = 'Computer', max_length=50)
	payment_method = models.CharField(default = 'Cash', max_length = 50)	# e.g. paypal, cash, venmo, etc
	price = models.FloatField(default=1.0)
	transaction_type = models.CharField(default = 'Selling', max_length=50) # e.g. buying, selling, or trading
	title = models.CharField(max_length=50)
	
	def __str__(self):
	
		return self.title
