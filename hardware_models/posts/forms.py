from django import forms
from django.forms import ModelForm
from django.utils import timezone
from .models import Post


class EditPostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
