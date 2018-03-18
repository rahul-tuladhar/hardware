from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
from django.urls import reverse
import urllib.parse
import json


# sends GET request to the URL(s) then returns a JsonResponse dictionary for homepage
def home(request):
    # get json response
    req = urllib.request.Request('http://models-api:8000/api/home/')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(json_response)

    # return
    return JsonResponse(context)


# sends a GET reqeust to the URL(s) then returns a JsonResponse for post_detail
def post_detail(request, id):
    # get json response
    req = urllib.request.Request('http://models-api:8000/api/post_detail/' + str(id))
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(json_response)

    # return
    return JsonResponse(context)


def register(request):
    # if method is POST
    if request.method == "POST":
        # get all the details posted from web layer
        detail = {'email': request.POST['email'], 'password': request.POST['password'],
                  'username': request.POST['username'], 'display_name': request.POST['display_name']}

        # pass encoded data to the model layer api
        enc_data = urllib.parse.urlencode(detail).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/api/register/', enc_data)

        # get the return json
        json_response = urllib.request.urlopen(req).read().decode('utf-8')
        context = json.loads(json_response)

        # return the JsonResponse
        return JsonResponse(context)

    # if trying to GET
    return HttpReponse("Error, cannot complete GET request")


def login(request):
    # if method is POST
    if request.method == "POST":
        # get all the details posted from web layer
        detail = {'password': request.POST['password'], 'username': request.POST['username']}

        # pass encoded data to the model layer api
        enc_data = urllib.parse.urlencode(detail).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/api/login/', enc_data)

        # get the return json
        json_response = urllib.request.urlopen(req).read().decode('utf-8')
        context = json.loads(json_response)

        # return the JsonResponse
        return JsonResponse(context)

    # if trying to GET
    return HttpReponse("Error, cannot complete GET request")


def logout(request):
    # if method is POST
    if request.method == "POST":
        # get the authenticator passed in from the web layer
        detail = {'authenticator': request.POST['authenticator']}

        # pass encoded data to the model layer api
        enc_data = urllib.parse.urlencode(detail).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/api/logout/', enc_data)

        # get the return json
        json_response = urllib.request.urlopen(req).read().decode('utf-8')
        context = json.loads(json_response)

        # return the JsonResponse
        return JsonResponse(context)

    # if trying to GET
    return HttpReponse("Error, cannot complete GET request")



    
