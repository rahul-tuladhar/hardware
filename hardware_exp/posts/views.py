from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json


#sends GET request to the URL(s) then returns a JsonResponse dictionary for homepage
def home(request):

    #get json response
    context = {}
    req = urllib.request.Request('http://models-api:8000/api/home')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    all_posts_dic = json.loads(json_response)

    #return
    return JsonResponse(context)


#sends a GET reqeust to the URL(s) then returns a JsonResponse for post_detail
def post_detail(request, id):

    #get json response
    req = urllib.request.Request('http://models-api:8000/api/post_detail/' + str(id))
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(json_response)

    #return
    return JsonResponse(context)
