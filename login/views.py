from django.shortcuts import render
from .models import Group, Profile
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict


# Create your views here.
def user_profile(request, username=None):
    # context = {}
    # if request.method == 'GET':
    #     try:
    #         profile = Profile.objects.get(username=username)
    #         context['profile'] = profile
    #     except ObjectDoesNotExist:
    #         return render(request, 'error.html')
    # return render(request, 'profile.html', context)

    if request.method == 'GET':
        try:
            profile = Profile.objects.get(username = username)
            x = model_to_dict(profile)
        except ObjectDoesNotExist:
            return JsonResponse({'status':'false','message':'ObjectDoesNotExist'}, status=500)
    

    if request.method == 'POST':
    	try:
    		profile = Profile.objects.get(username = username)
    		x = model_to_dict(profile)
    		return JsonResponse({'status': 'true', 'message': 'Cannot edit'})
    	except ObjectDoesNotExist:
    		return JsonResponse({'status': 'false', 'message': 'ObjectDoesNotExist'})
  
    del x['affiliations']
    return JsonResponse(x, safe=False)


