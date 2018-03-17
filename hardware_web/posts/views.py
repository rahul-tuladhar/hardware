from django.shortcuts import render
import urllib.request
import urllib.parse
import json
from django.http import HttpResponse
#from .forms import AddPostForm


#sends GET request to the URL then returns a JsonResponse dictionary for homepage
def home(request):

    #get the json response
    req = urllib.request.Request('http://exp-api:8000/api/home/')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    response = json.loads(json_response)

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
    if request.method = 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            values = {}
            values['author'] = form.cleaned_data['author']
            values['date'] = form.cleaned_data['date']
            values['description'] = form.cleaned_data['description']
            values['location'] = form.cleaned_data['location']
            values['part'] = form.cleaned_data['part']
            values['payment_method'] = form.cleaned_data['payment_method']
            values['price'] = form.cleaned_data['price']
            values['transaction_type'] = form.cleaned_data['transaction_type']
            values['title'] = form.cleaned_data['title']
            data = urllib.parse.urlencode(values)
            req = urllib.request.Request('http://exp-api:8000/api/add_post/', data)
            json_response = urllib.request.urlopen(req)
            response = json.loads(json_response)
            return render(request, 'index.html')
        else:
            return render(request, 'add_post.html', {'form': form})
    else:
        form = AddPostForm()

    return render(request, 'add_post.html', {'form': form})
