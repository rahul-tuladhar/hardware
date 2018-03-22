from django import forms
from django.utils import timezone


class AddPostForm(forms.Form):
    TRANSACTION_TYPES = (
        ('BUYING', 'Buying'),
        ('SELLING', 'Selling'),
        ('TRADING', 'Trading'),
    )
    author = forms.CharField(label='Poster username', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control'}))
    location = forms.CharField(label='Location', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    part = forms.CharField(label='Part', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    payment_method = forms.CharField(label='Payment method', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class': 'form-control'}))
    transaction_type = forms.CharField(label='Transaction type', max_length=7, widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label='Title', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))


class RegistrationForm(forms.Form):

	username = forms.CharField(label='Username: ', max_length=24)
	display_name = forms.CharField(label='First and Last Name: ', max_length=24)
	email = forms.EmailField(label='Email: ', max_length=254)
	password = forms.CharField(label='Password: ', widget=forms.PasswordInput())


class LoginForm(forms.Form):

	username = forms.CharField(label='Username: ', max_length=24)
	password = forms.CharField(label='Password: ', widget=forms.PasswordInput())

