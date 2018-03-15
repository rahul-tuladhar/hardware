from django.shortcuts import render
import urllib.request
import urllib.parse
import json

def homepage(request):
    #get the json response
    req = urllib.request.Request('http://exp-api:8000/api/v3/users/home')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    response = json.loads(json_response)

    #set the context to be just the post data from the response object
    context = {
        'data': response['users']['result']
    }

    #render the data with the html
    return render(request, 'index.html', context)
