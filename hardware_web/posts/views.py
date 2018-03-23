from django.shortcuts import render
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.contrib.auth.hashers import make_password

# sends GET request to the URL then returns a JsonResponse dictionary for homepage
def home(request):

    req = requests.get('http://exp-api:8000/api/home/')
    response = req.json()

    context = {
        'data': response['result'].values(),
    }

    return render(request, 'index.html', context)

# sends a GET reqeust to the URL then returns a JsonResponse for post_detail
def post_detail(request, id):
    # get the json response
    req = requests.get('http://exp-api:8000/api/post_detail/' + str(id))

    # set the context to be the single post
    context = req.json()
    return render(request, 'post_detail.html', context)


# check to see if the user is already logged in
def check_auth(request):

    # if some cookie exists
    if request.COOKIES.get('authenticator'):

        detail = {'authenticator': request.COOKIES.get('authenticator')}

        #pass encoded data to the experience layer api
        req = requests.post('http://exp-api:8000/api/check_auth/', data=detail)

        #get the return json
        context = req.json()

        #return the status
        return context['status']

    return False;


# add a post
def add_post(request):

    #check to see if user is authenticated
    if not check_auth(request):

        return render(request, 'not_auth.html') 


    if request.method == 'POST':

        form = AddPostForm(request.POST)

        if form.is_valid():
            data = {
                'author': form.cleaned_data['author'],
                'description': form.cleaned_data['description'],
                'location': form.cleaned_data['location'],
                'part': form.cleaned_data['part'],
                'payment_method': form.cleaned_data['payment_method'],
                'price': form.cleaned_data['price'],
                'transaction_type': form.cleaned_data['transaction_type'],
                'title': form.cleaned_data['title'],
            }
            req = requests.post('http://exp-api:8000/api/add_post/', data = data)
            response = req.json()

            context = {'status': response['status'],}

            if (context['status']): # the model was successfully added
                return HttpResponseRedirect('/home/')

            else:   # the model was not successfully added
                form = AddPostForm()
                return render(request, 'index.html', {'form': form})

        else: # the form was not valid
            form = AddPostForm()
            return render(request, 'index.html', {'form': form})

    else:   # GET request; load a blank form
        form = AddPostForm()
   

    return render(request, 'add_post.html', {'form': form})

# register a user
@csrf_exempt
def register(request):
    # if request is POST, must process data from form
    if request.method == 'POST':

        # create form instance and populate it with data from the request
        form = RegistrationForm(request.POST)

        # check whether the form is valid
        if form.is_valid():

            #process data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            display_name = form.cleaned_data['display_name']

            detail = {'email': email, 'password': password, 'username': username, 'display_name': display_name}

            #pass encoded data to the experience layer api
            req = requests.post('http://exp-api:8000/api/register/', data=detail)

            #get the return json
            context = req.json()

            #error checking
            if not context:
                return render(request, 'register.html', {'error': 'Failed to register user', 'form': RegistrationForm()})
            if context['status'] != True:
                return render(request, 'register.html', {'error': context['result'], 'form': RegistrationForm()})

            #redirect to the login page after everything is done
            return HttpResponseRedirect(reverse('login'))

        # if form is not valid send an error
        else:
            return render(request, 'register.html') 

    # if request is GET, render the blank form
    return render(request, 'register.html', {'form': RegistrationForm()})



# login view
@csrf_exempt
def login(request):

    # if request is POST, must process data from form
    if request.method == 'POST':

        # see if the user is already logged in
        if request.COOKIES.get('authenticator'):

            # fail to login
            return render(request, 'login.html', {'error': 'Please logout before logging in again', 'form': LoginForm()})

        # create form instance and populate it with data from the request
        form = LoginForm(request.POST)

        # check whether the form is valid
        if form.is_valid():

            # process data
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']

            detail = {'password': password, 'username': username}

            # pass encoded data to the experience layer api
            req = requests.post('http://exp-api:8000/api/login/', data=detail)

            # get the return json
            context = req.json()

            # error checking
            if not context:
                return render(request, 'login.html', {'error': "Login failed", 'form': LoginForm()})
            if context['status'] != True:
                return render(request, 'login.html', {'error': context['result'], 'form': LoginForm()})

            # logged in successfully, go to home page and set cookie
            response = HttpResponseRedirect(reverse('home'))
            response.set_cookie('authenticator', context['result'])

            # return response 
            return response

        # if form is not valid send an error
        else:
            return render(request, 'login.html', {'error': 'Error logging in', 'form': LoginForm()})

    # if request is GET, render the blank form
    return render(request, 'login.html', {'form': LoginForm()})


# logout view
@csrf_exempt
def logout(request):

    #if post
    if request.method == "POST":

        #if an authenticator cookie exists
        if request.COOKIES.get('authenticator'):

            # get the authenticator for the user
            detail = {'authenticator': request.COOKIES.get('authenticator')}

            #pass encoded data to the experience layer api
            req = requests.post('http://exp-api:8000/api/logout/', data=detail)

            #get the return json
            context = req.json()

            # error checking
            if (not context) or (context['status'] != True):
                return render(request, 'logout.html', {'error': context['result']})

            #delete the cookie
            response = render(request, 'logout.html', {'result': context['result']})
            response.delete_cookie('authenticator') 

            #go to logout screen
            return response

        return render(request, 'logout.html', {'error': 'You are not logged in'})

    #if GET
    return render(request, 'logout.html')

