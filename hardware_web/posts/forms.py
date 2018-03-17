from django import forms

class RegistrationForm(forms.Form):

	username = forms.CharField(label='Username: ', max_length=24)
	display_name = forms.CharField(label='First and Last Name: ', max_length=24)
	email = forms.EmailField(label='Email: ', max_length=254)
	password = forms.CharField(label='Password: ', widget=forms.PasswordInput())


class LoginForm(forms.Form):

	username = forms.CharField(label='Username: ', max_length=24)
	password = forms.CharField(label='Password: ', widget=forms.PasswordInput())