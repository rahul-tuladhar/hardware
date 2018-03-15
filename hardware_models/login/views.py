from django.shortcuts import render
from login.models import Group, Profile
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import JsonResponse
from django.core import serializers
import urllib.request
import urllib.parse


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

def index(request):
    if request.method == 'GET':
        #result dictionary
        all_profiles_dict = {}
        try:
            #getting all of the posts
            all_profiles = Profile.objects.all().values()
            #append each post to a dictionary
            ### all_profiles seems to error out and cause a 500 error
            # for profile in all_profiles:
            #     all_profiles_dict[profile['id']] = profile
            #response object showing that it worked

            response = {'status': True, 'result': {'test': False}}
            #return json object with success message
            return JsonResponse(response, safe=False)

        except ObjectDoesNotExist:

            #response object showing that it failed
            response = {'status': False, 'result': all_profiles_dict}

            #return json object with failure message
            return JsonResponse(response, safe=False)

    #if attempting to save data to DB
    if request.method == 'POST':
        # all_profiles = Profile.objects.all().values()
        all_profiles_dict = {'status': 'Nothing to POST'}


    return JsonResponse(all_profiles_dict, safe=False)
