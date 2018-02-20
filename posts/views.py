from django.shortcuts import render
from .models import Post
from .forms import PostEditForm
from django.http import JsonResponse
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

    all_posts = Post.objects.all().values()
    post_list = list(all_posts)
    return JsonResponse(post_list, safe=False)

def post_detail(request, post_title=None):
    if request.method == 'GET':
        try:
            post = Post.objects.get(title=post_title).values()
            post = list(post)
        except ObjectDoesNotExist:
            post = {'error': 'object does not exist'}
    return JsonResponse(post)

def edit_post(request, post_title=None):
    # context = {}
    if request.method == 'GET':
        return JsonResponse({'form': 'form is blank'})
    if request.method == 'POST':
        return JsonResponse({'form': 'form submitted successfully'})
    # else:
    #     try:
    #         post = Post.objects.get(title=post_title)
    #         context['post'] = post
    #         form = PostEditForm(request.POST, instance=post)
    #         context['form'] = form
    #     except ObjectDoesNotExist:
    #         return render(request, 'error.html')
    #     return render(request, 'edit_post.html', context)
