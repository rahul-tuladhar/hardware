from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json


# Create your views here.
def homepage(request):
    """ Sends GET request to the URL(s) then returns a JsonResponse dictionary for homepage """
    # TODO: error checking and exception handling

    context = {}
    req = urllib.request.Request('http://models-api:8000/api/v3/posts/home')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    all_posts_dic = json.loads(json_response)
    context["posts"] = all_posts_dic    # adds posts dict to separate requested information
    return JsonResponse(context)


def post_detail(request, id):
    """ Sends a GET reqeust to the URL(s) then returns a JsonResponse for post_detail """
    # TODO: error checking and exception handling
    req = urllib.request.Request('http://models-api:8000/api/v3/posts/' + str(id))
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(json_response)
    return JsonResponse(context)
