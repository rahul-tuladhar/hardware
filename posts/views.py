from django.shortcuts import render
from .models import Post
from .forms import PostEditForm
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
import json

# Create your views here.
# def index(request):
#     # response = JsonResponse(some_dictionary)
#     context = {}
#     all_posts = Post.objects.all()
    
#     context['posts'] = all_posts
#     return JsonResponse(context)
# =======

# Create your views here.
def index(request):
    # context = {}
    # all_posts = Post.objects.all()
    # context['posts'] = all_posts
    # return render(request, 'index.html', context
    if request.method == 'GET':
        try:
            all_posts = Post.objects.all()
            all_posts_dict = model_to_dict(all_posts)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'ObjectDoesNotExist'})
    return JsonResponse(all_posts_dict, safe=False)

def post_detail(request, post_title=None):
    if request.method == 'GET':
        try:
            post = Post.objects.get(title=post_title)
            post_dict = model_to_dict(post)
            del post_dict['image']
        except ObjectDoesNotExist:
            post_dict = {'error': 'object does not exist'}
    if request.method == 'POST':
        return JsonResponse({'status': 'nothing to POST, only viewing a post detail'})
    return JsonResponse(post_dict, safe = False)


def edit_post(request, post_title=None, post_author= None, post_description= None, post_price = None ):
    # context = {}
    if request.method == 'GET':
        return JsonResponse({'status': 'should not get request edit_post'})
    if request.method == 'POST':
        try:
            post = Post.objects.get(title=post_title)
            # if (request.POST is not None):
            #     post.title = post_title
            # if (post_description is not None):
            #     post.description = post_description
            # if (post_author is not None):
            #     post.author = post_author
            # if (post_price is not None):  
            #     post.price = float(post_price)
            # post.save() 
            post_dict = model_to_dict(post)
            del post_dict['image']
        except ObjectDoesNotExist:
            return JsonResponse({'status': False})
        return JsonResponse(post_dict, safe=False)
        
    # else:
    #     try:
    #         post = Post.objects.get(title=post_title)
    #         context['post'] = post
    #         form = PostEditForm(request.POST, instance=post)
    #         context['form'] = form
    #     except ObjectDoesNotExist:
    #         return render(request, 'error.html')
    #     return render(request, 'edit_post.html', context)
