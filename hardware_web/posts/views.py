from django.shortcuts import render
import requests
from django.http import HttpResponse,  HttpResponseRedirect
from .forms import AddPostForm


#sends GET request to the URL then returns a JsonResponse dictionary for homepage
def home(request):

    #get the json response
    req = requests.get('http://exp-api:8000/api/home/')
    response = req.json()

    context = {
        'data': response['result'].values(),
    }

    return render(request, 'index.html', context)

#sends a GET reqeust to the URL then returns a JsonResponse for post_detail
def post_detail(request, id):

    #get the json response
    req = requests.get('http://exp-api:8000/api/post_detail/' + str(id))
    response = req.json()

    #set the context to be the single post
    context = response

    return render(request, 'post_detail.html', context)


def add_post(request):
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
