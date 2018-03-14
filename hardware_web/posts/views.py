from django.shortcuts import render
import urllib.request
import urllib.parse
import json
from django.http import HttpResponse


#sends GET request to the URL then returns a JsonResponse dictionary for homepage
def homepage(request):

    #get the json response
    req = urllib.request.Request('http://exp-api:8000/api/v3/posts/home')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    response = json.loads(json_response)

    #set the context to be just the post data from the response object
    context = {
        'data': response['posts']['result']
    }

    #render the data with the html
    return render(request, 'index.html', context)


def post_detail(request, id):
    """ Sends a GET reqeust to the URL then returns a JsonResponse for post_detail """

    req = urllib.request.Request('http://exp-api:8000/api/v3/posts/' + str(id))
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(json_response)
    return render(request, 'post_detail.html', context)
