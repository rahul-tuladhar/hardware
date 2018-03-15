from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json

# Create your views here.
def homepage(request):

    #get json response
    context = {}
    users_req = urllib.request.Request('http://models-api:8000/api/v3/users/profile')
    users_response = urllib.request.urlopen(users_req).read().decode('utf-8')
    all_profiles_dict = json.loads(users_response)

    #adds posts dict to separate requested information
    context["profiles"] = all_profiles_dict

    #return
    return JsonResponse(context)
