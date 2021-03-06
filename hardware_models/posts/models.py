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
    # affiliations = models.ManyToManyField(Group)
    display_name = models.CharField(max_length=24)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=24, default='N/A', unique=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    TRANSACTION_TYPES = (
        ('BUYING', 'Buying'),
        ('SELLING', 'Selling'),
        ('TRADING', 'Trading'),
    )
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=2048)
    location = models.CharField(default='JPA', max_length=24)
    part = models.CharField(default='Computer', max_length=50)
    payment_method = models.CharField(default='Cash', max_length=50)  # e.g. paypal, cash, venmo, etc
    price = models.FloatField(default=1.0)
    transaction_type = models.CharField(choices=TRANSACTION_TYPES,  max_length=7)  # e.g. buying, selling, or trading
    title = models.CharField(max_length=50)

    def __str__(self):
        """
        :return: Returns the title string.
        """
        return self.title


class Authenticator(models.Model):
    """ Authenticator holds a large random value associated with a user id """
    auth = models.CharField(max_length=255, primary_key=True)  # large random value as character field for now
    date_created = models.DateTimeField(default=timezone.now)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        """
        :return: Returns the title string.
        """
        return self.auth

class Recommendation(models.Model):
    item_id = models.IntegerField(primary_key=True, default = 0)
    rec_items = models.CharField(max_length=200)
