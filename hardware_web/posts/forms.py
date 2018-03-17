from django import forms
from django.utils import timezone


class AddPostForm(forms.Form):
    TRANSACTION_TYPES = (
        ('BUYING', 'Buying'),
        ('SELLING', 'Selling'),
        ('TRADING', 'Trading'),
    )
    author = forms.CharField(label='Poster username', max_length=50)
    date = forms.DateTimeField(label='Date', default=timezone.now)
    description = forms.TextField(label='Description', max_length=2048)
    location = forms.CharField(label='Description', default='JPA', max_length=100)
    part = forms.CharField(label='Part', default='Computer', max_length=50)
    payment_method = forms.CharField(label='Payment method', default='Cash', max_length=10)
    price = forms.FloatField(label='Price', default=1.0)
    transaction_type = forms.CharField(label='Transaction type', choices=TRANSACTION_TYPES, max_length=7)
    title = forms.CharField(label='Title', max_length=50)
