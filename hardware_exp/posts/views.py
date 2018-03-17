from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json


#sends GET request to the URL(s) then returns a JsonResponse dictionary for homepage
def home(request):

    #get json response
    req = urllib.request.Request('http://models-api:8000/api/home/')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(json_response)

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

def add_post(request):

    if request.method == 'POST':
        values = {
        'author': request.POST['author'],
        'date': request.POST['date'],
        'description': request.POST['description'],
        'location': request.POST['location'],
        'part': request.POST['part'],
        'payment_method': request.POST['payment_method'],
        'price': request.POST['price'],
        'transaction_type': request.POST['transaction_type'],
        'title': request.POST['title'],
        }
        data = urllib.parse.urlencode(values).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/api/add_post', data)
        json_response = urllib.request.urlopen(req).read().decode('utf-8')
        context = json.loads(json_response)

        return JsonResponse(context)
