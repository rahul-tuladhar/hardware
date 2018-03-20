from django.shortcuts import render
import urllib.request
import urllib.parse
import requests
import json
from django.http import HttpResponse,  HttpResponseRedirect
from .forms import AddPostForm


#sends GET request to the URL then returns a JsonResponse dictionary for homepage
def home(request):

    #get the json response
    req = requests.get('http://exp-api:8000/api/home/')
    response = req.json()

    context = {
        'data': response['result'],
    }

    return render(request, 'index.html', context)

#sends a GET reqeust to the URL then returns a JsonResponse for post_detail
def post_detail(request, id):

    #get the json response
    req = urllib.request.Request('http://exp-api:8000/api/post_detail/' + str(id))
    json_response = urllib.request.urlopen(req).read().decode('utf-8')

    #set the context to be the single post
    context = json.loads(json_response)

    return render(request, 'post_detail.html', context)


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = {}
            data['author'] = form.cleaned_data['author']
            data['description'] = form.cleaned_data['description']
            data['location'] = form.cleaned_data['location']
            data['part'] = form.cleaned_data['part']
            data['payment_method'] = form.cleaned_data['payment_method']
            data['price'] = form.cleaned_data['price']
            data['transaction_type'] = form.cleaned_data['transaction_type']
            data['title'] = form.cleaned_data['title']
            req = requests.post('http://exp-api:8000/api/add_post', data = data)
            return HttpResponseRedirect('/home/')
        else:
            form = AddPostForm()
            return render(request, 'add_post.html', {'form': form})
    else:   # GET request; load a blank form
        form = AddPostForm()

    return render(request, 'add_post.html', {'form': form})
