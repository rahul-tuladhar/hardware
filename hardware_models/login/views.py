from django.shortcuts import render
from .models import Group, Profile
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict


# Create your views here.
def user_profile(request, username=None):
    """
    :param request: HTTP request
    :param username: Given username for retrieving object attributes
    :return: JsonResponse of serialized attributes
    """

    if request.method == 'GET':
        try:
            profile = Profile.objects.get(username=username)
            x = model_to_dict(profile)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'ObjectDoesNotExist'}, status=500)

    if request.method == 'POST':
        try:
            profile = Profile.objects.get(username=username)
            x = model_to_dict(profile)
            return JsonResponse({'status': 'true', 'message': 'Cannot edit'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'ObjectDoesNotExist'})

    del x['affiliations']
    return JsonResponse(x, safe=False)
