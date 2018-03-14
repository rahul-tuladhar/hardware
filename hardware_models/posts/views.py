from django.shortcuts import render
from .models import Post
from .forms import PostEditForm
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
import json


# Create your views here.
def index(request):
    """  Returns a JsonResponse dictionary with all of the Post objects' attributes. """

    if request.method == 'GET':
        try:
            all_posts_dict = {}
            all_posts = Post.objects.all().values()
            for post in all_posts:
                all_posts_dict[post['id']] = post
        except ObjectDoesNotExist:
            all_posts_dict = {'status': 'ObjectDoesNotExist'}
    if request.method == 'POST':
        try:
            all_posts = Post.objects.all().values()
            all_posts_dict = {'status': 'Nothing to POST'}
        except ObjectDoesNotExist:
            all_posts_dict = {'status': 'ObjectDoesNotExist'}
    return JsonResponse(all_posts_dict, safe=False)


def post_detail(request, id):
    """
    :param request: HTTP request
    :param post_id: ID of the specific post
    :return: JsonResponse dictionary with given attributes.
    """

    if request.method == 'GET':
        try:
            post = Post.objects.get(id=id)
            post_dict = model_to_dict(post)
            del post_dict['image'] 
        except ObjectDoesNotExist:
            post_dict = {'error': 'object does not exist'}
    if request.method == 'POST':
        post_dict = {'status': 'nothing to POST, only viewing a post detail'}
    return JsonResponse(post_dict, safe=False)


def edit_post(request, id):
    """
    Returns a JsonResponse dictionary of a post during a POST Request.
    :param request:
    :param post_title:
    :param post_author:
    :param post_description:
    :param post_price:
    :return:
    """
    if request.method == 'GET':
        post_dict = {'status': 'should not get request edit_post'}
    # TODO: Fully implement the entity API layer of this method
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=id)
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
            post_dict = {'status': 'ObjectDoesNotExist'}
    return JsonResponse(post_dict, safe=False)
