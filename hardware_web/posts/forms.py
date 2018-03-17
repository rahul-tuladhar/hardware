from django import forms

class RegistrationForm(forms.Form):

	username = forms.CharField(label='', max_length=24)
	display_name = forms.CharField(label='', max_length=24)
	email = forms.EmailField(label='', max_length=254)
	password = forms.CharField(label='', widget=forms.PasswordInput())


class LoginForm(forms.Form):

	username = forms.CharField(label='', max_length=24)
	password = forms.CharField(label='', widget=forms.PasswordInput())