from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import json

# Create your views here.
# def user_profile(request, username=None):
#     context = {}
#     if request.method == 'GET':
#         try:
#             profile = Profile.objects.get(username=username)
#             context['profile'] = profile
#         except ObjectDoesNotExist:
#             return render(request, 'error.html')
#     return render(request, 'profile.html', context)

def homepage(request):
    #get the json response
    req = urllib.request.Request('http://exp-api:8000/api/v3/users/home')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    response = json.loads(json_response)

    #set the context to be just the post data from the response object
    context = {
        'data': response['users']['result']
    }

    #render the data with the html
    return render(request, 'index.html', context)
