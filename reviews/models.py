from django.db import models
from posts.models import Post
from login.models import Profile
from django.utils import timezone


# Create your models here.
class Review(models.Model):
    """ Attributes in alphabetical order"""
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=2048)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    rating = models.FloatField(default=5.0)
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        """
        Return the title as the string
        :return:
        """
        return self.title
