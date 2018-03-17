from django.shortcuts import render
import urllib.request
import urllib.parse
from django.http import HttpResponse
import json
from .forms import *

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

#register a user
def register(request):

    # #if request is POST, must process data from form
    # if request.method == 'POST':

    #     #create form instance and populate it with data from the request
    #     form = RegistrationForm(request.POST)

    #     #check whether the form is valid
    #     if form.is_valid():

    #         #process data
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         username = form.cleaned_data['username']
    #         display_name = form.cleaned_data['display_name']

    #         detail = {'email': email, 'password': password, 'username': username, 'display_name': display_name}

    #         ######do more stuff here###########

    #     #if form is not valid send an error
    #     else:
    #         return render(request, 'register.html')


    #if request is GET, render the blank form
    return render(request, 'register.html', {'form' : RegistrationForm()})

#login
def login(request):

    #do stuff
    return render(request, 'register.html', {'form' : RegistrationForm()})

#logout
def logout(request):

    return render(request, 'register.html', {'form' : RegistrationForm()})
    #do stuff









