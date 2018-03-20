from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import urllib.parse
import requests
import json


#sends GET request to the URL(s) then returns a JsonResponse dictionary for homepage
def home(request):

    req = requests.get('http://models-api:8000/api/home/')
    context = req.json()

    return JsonResponse(context)

#sends a GET reqeust to the URL(s) then returns a JsonResponse for post_detail
def post_detail(request, id):

    #get json response
    req = urllib.request.Request('http://models-api:8000/api/post_detail/' + str(id))
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(json_response)

    #return
    return JsonResponse(context)

def add_post(request):
    if (request.method == 'POST'):
        data = {
        'author': request.POST.get('author'),
        'description': request.POST.get('description'),
        'location': request.POST.get('location'),
        'part': request.POST.get('part'),
        'payment_method': request.POST.get('payment_method'),
        'price': request.POST.get('price'),
        'transaction_type': request.POST.get('transaction_type'),
        'title': request.POST.get('title'),
        }

        req = requests.post('http://models-api:8000/api/add_post', data = data)
        context = {'status': 'ok'}
        return JsonResponse(context)
