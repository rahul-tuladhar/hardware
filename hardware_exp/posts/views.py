from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
from django.urls import reverse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import is_password_usable, make_password
from elasticsearch import Elasticsearch
from kafka import KafkaProducer
import json


# sends GET request to the URL(s) then returns a JsonResponse dictionary for homepage
def home(request):
    # get json response
    req = requests.get('http://models-api:8000/api/home/')
    context = req.json()

    return JsonResponse(context)


def search_posts(request):
    es = Elasticsearch(['es'])
    resp = es.search(index='listing_index', body={'query': {'query_string': {'query': request.GET.get('title')}}, 'size': 10})
    return JsonResponse(resp)

# details of a post
def post_detail(request, id):
    # get json response
    req = requests.get('http://models-api:8000/api/post_detail/' + str(id))
    context = req.json()

    # get json response
    req = requests.get('http://models-api:8000/api/post_detail/' + str(id))
    response = req.json()

    context = response
    return JsonResponse(context)


# see if authenticator is in database
@csrf_exempt
def check_auth(request):
    # if method is POST
    # if request.method == "POST":
    if request.COOKIES.get('authenticator'):
        # pass encoded data to the model layer api
        req = requests.get('http://models-api:8000/api/check_auth/', cookies=request.COOKIES)

        # get the return json
        if req.status_code == 200:
            context = req.json()
        else:
            context = {'status': False, 'error': 'reqs raised a 500 error'}
        # return the JsonResponse
        return JsonResponse(context)


# add a new post
def add_post(request):
    if request.method == 'POST':
        data = {
            # 'author': request.POST.get('author'),
            'description': request.POST.get('description'),
            'location': request.POST.get('location'),
            'part': request.POST.get('part'),
            'payment_method': request.POST.get('payment_method'),
            'price': request.POST.get('price'),
            'transaction_type': request.POST.get('transaction_type'),
            'title': request.POST.get('title'),
        }
        req = requests.post('http://models-api:8000/api/add_post/', data=data, cookies= request.COOKIES)
        if req.status_code == 200:
            context = req.json()
        else:
            context = {'status': False, 'error': 'reqs raised a 500 error'}
        return JsonResponse(context, safe=False)
    else:  # GET request
        context = {'status': False}
        return JsonResponse(context, safe=False)


# register a new user
@csrf_exempt
def register(request):
    # if method is POST
    if request.method == "POST":
        if is_password_usable(request.POST['password']):
            # get all the details posted from web layer
            detail = {'email': request.POST['email'], 'password': request.POST['password'],
                      'username': request.POST['username'], 'display_name': request.POST['display_name']}

            # pass data to model layer api
            req = requests.post('http://models-api:8000/api/register/', data=detail)

            # get the return json
            context = req.json()

            # return the JsonResponse
            return JsonResponse(context)
        # else:
        #     context = {
        #         'status': False,
        #         'result': 'Password is not usable'
        #     }
        #     return JsonResponse(context)

    # if trying to GET
    return HttpResponse("Error, cannot complete GET request")


@csrf_exempt
def login(request):
    # if method is POST
    if request.method == "POST":
        # get all the details posted from web layer
        detail = {'password': request.POST['password'], 'username': request.POST['username']}

        # pass encoded data to the model layer api
        req = requests.post('http://models-api:8000/api/login/', data=detail)

        # get the return json
        context = req.json()

        # return the JsonResponse
        return JsonResponse(context)

    # if trying to GET
    return HttpResponse("Error, cannot complete GET request")


@csrf_exempt
def logout(request):
    # if method is POST
    if request.method == "POST":
        # get the authenticator passed in from the web layer
        detail = {'authenticator': request.POST['authenticator']}

        # pass encoded data to the model layer api
        req = requests.post('http://models-api:8000/api/logout/', data=detail)

        # get the return json
        context = req.json()

        # return the JsonResponse
        return JsonResponse(context)

    # if trying to GET
    return HttpResponse("Error, cannot complete GET request")
