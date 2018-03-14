from django.shortcuts import render
import urllib.request
import urllib.parse
import json
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    """ Sends GET request to the URL then returns a JsonResponse dictionary for homepage """

    req = urllib.request.Request('http://exp-api:8000/api/v3/posts/home')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(json_response)
    return render(request, 'index.html', context)


def post_detail(request, id):
    """ Sends a GET reqeust to the URL then returns a JsonResponse for post_detail """

    req = urllib.request.Request('http://exp-api:8000/api/v3/posts/' + str(id))
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(json_response)
    return render(request, 'post_detail.html', context)
