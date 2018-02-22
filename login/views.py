from django.shortcuts import render
from .models import Group, Profile
from django.core.exceptions import ObjectDoesNotExist
import json

# Create your views here.
def user_profile(request, username=None):
    context = {}
    if request.method == 'GET':
        try:
            profile = Profile.objects.get(username=username)
            context['profile'] = profile
        except ObjectDoesNotExist:
            return render(request, 'error.html')
    return render(request, 'profile.html', context)
