from django.shortcuts import render
import urllib.request
import urllib.parse
from django.http import HttpResponse
import json
from django.urls import reverse
from .forms import *


# sends GET request to the URL then returns a JsonResponse dictionary for homepage
def home(request):
    # get the json response
    req = urllib.request.Request('http://exp-api:8000/api/home/')
    json_response = urllib.request.urlopen(req).read().decode('utf-8')
    response = json.loads(json_response)

    context = {
        'data': response['result'],
    }

    # render the data with the html
    return render(request, 'index.html', context)


# sends a GET reqeust to the URL then returns a JsonResponse for post_detail
def post_detail(request, id):
    # get the json response
    req = urllib.request.Request('http://exp-api:8000/api/post_detail/' + str(id))
    json_response = urllib.request.urlopen(req).read().decode('utf-8')

    # set the context to be the single post
    context = json.loads(json_response)

    # return
    return render(request, 'post_detail.html', context)


# register a user
def register(request):
    # if request is POST, must process data from form
    if request.method == 'POST':

        # create form instance and populate it with data from the request
        form = RegistrationForm(request.POST)

        # check whether the form is valid
        if form.is_valid():

            # #process data
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # username = form.cleaned_data['username']
            # display_name = form.cleaned_data['display_name']

            # detail = {'email': email, 'password': password, 'username': username, 'display_name': display_name}

            # #pass encoded data to the experience layer api
            # enc_data = urllib.parse.urlencode(detail).encode('utf-8')
            # req = urllib.request.Request('http://exp-api:8000/api/register/', enc_data)

            # #get the return json
            # json_response = urllib.request.urlopen(req).read().decode('utf-8')
            # context = json.loads(json_response)

            # #error checking
            # if not context['status'] or not context:
            #     return render(request, 'register.html', {'error': "Registration failed", 'form': RegistrationForm()})

            #redirect to the login page after everything is done
            return HttpResponse(reverse('home'))

        # if form is not valid send an error
        else:
            return render(request, 'register.html') 

    # if request is GET, render the blank form
    return render(request, 'register.html', {'form': RegistrationForm()})


# login view
def login(request):
    # if request is POST, must process data from form
    if request.method == 'POST':

        # create form instance and populate it with data from the request
        form = LoginForm(request.POST)

        # check whether the form is valid
        if form.is_valid():

            # process data
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']

            detail = {'password': password, 'username': username}

            # pass encoded data to the experience layer api
            enc_data = urllib.parse.urlencode(detail).encode('utf-8')
            req = urllib.request.Request('http://exp-api:8000/api/login/', enc_data)

            # get the return json
            json_response = urllib.request.urlopen(req).read().decode('utf-8')
            context = json.loads(json_response)

            # error checking
            if not context['status'] or not context:
                return render(request, 'register.html', {'error': "Login failed", 'form': LoginForm()})

            # get returned authenticator
            authenticator = context['result']

            # logged in successfully, go to home page and set cookie
            response = HttpResponseRedirect(reverse('home'))
            response.set_cookie('authenticator', authenticator)

            return response

        # if form is not valid send an error
        else:
            return render(request, 'login.html', {'error': 'Error logging in', 'form': LoginForm()})

    # if request is GET, render the blank form
    return render(request, 'login.html', {'form': LoginForm()})


# logout view
def logout(request):
    # #get the authenticator for the user
    # detail = {'authenticator': request.COOKIES['authenticator']}

    # #pass encoded data to the experience layer api
    # enc_data = urllib.parse.urlencode(detail).encode('utf-8')
    # req = urllib.request.Request('http://exp-api:8000/api/logout/', enc_data)

    # #get the return json
    # json_response = urllib.request.urlopen(req).read().decode('utf-8')
    # context = json.loads(json_response)

    # #delete the cookie
    # response = HttpResponseRedirect(reverse('home'))
    # response.delete_cookie('authenticator') 

    # return the successful logout page
    return render(request, 'logout.html')
