from django.shortcuts import render
import urllib.request
import urllib.parse
import json
from django.http import HttpResponse


#sends GET request to the URL then returns a JsonResponse dictionary for homepage
def home(request):

    #get the json response
    req = urllib.request.Request('http://exp-api:8000/api/home/')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    response = json.loads(json_response)

    context = {
        'data': response['result'],
    }

    #render the data with the html
    return render(request, 'index.html', context)

#sends a GET reqeust to the URL then returns a JsonResponse for post_detail
def post_detail(request, id):

    #get the json response
    req = urllib.request.Request('http://exp-api:8000/api/post_detail/' + str(id))
    json_response = urllib.request.urlopen(req).read().decode('utf-8')

    #set the context to be the single post
    context = json.loads(json_response)

    #return
    return render(request, 'post_detail.html', context)
