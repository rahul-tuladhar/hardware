from django.shortcuts import render
from django.http import JsonResponse
import requests

#sends GET request to the URL(s) then returns a JsonResponse dictionary for homepage
def home(request):

    req = requests.get('http://models-api:8000/api/home/')
    context = req.json()

    return JsonResponse(context)

#sends a GET reqeust to the URL(s) then returns a JsonResponse for post_detail
def post_detail(request, id):

    #get json response
    req = requests.get('http://models-api:8000/api/post_detail/' + str(id))
    response = req.json()

    context = response

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
        req = requests.post('http://models-api:8000/api/add_post/', data=data)
        context = req.json()
        return JsonResponse(context, safe=False)
    else: # GET request
        context = {'status': False}
        return JsonResponse(context, safe=False)
