from django.shortcuts import render
import urllib.request
import urllib.parse
import json

# Create your views here.
def homepage(request):
    req = urllib.request.Request('http://localhost:8000/v3/exp/posts/home')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(json_response)
    return render(response, 'home.html', context)
