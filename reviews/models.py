from django.db import models
from posts.models import Post
from login.models import User
import timezone

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    rating = models.FloatField(default=5.0)
    upvotes = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now())
    description = models.TextField(max_length=2048)
    post = models.OneToOneField(Post)
    reviewer = models.ForeignKey(User)
