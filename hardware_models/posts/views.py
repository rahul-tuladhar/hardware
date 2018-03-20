from .models import Post
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict

# returns a JsonResponse dictionary with all of the Post objects' attributes
def home(request):

    # result dictionary
    all_posts_dict = {}

    # if attempting to get data from DB
    if request.method == 'GET':
        try:
            # getting all of the posts
            all_posts = Post.objects.all().values()
            # append each post to a dictionary
            for post in all_posts:
                all_posts_dict[post['id']] = post
            # response object showing that it worked
            response = {'status': True, 'result': all_posts_dict}
            # return json object with success message
            return JsonResponse(response, safe=False)
        except ObjectDoesNotExist:
            # response object showing that it failed
            response = {'status': False, 'result': all_posts_dict}
            # return json object with failure message
            return JsonResponse(response, safe=False)
    # if attempting to save data to DB
    if request.method == 'POST':
        all_posts = Post.objects.all().values()
        all_posts_dict = {'status': 'Nothing to POST'}
    return JsonResponse(all_posts_dict, safe=False)

# returns the details of a specific post
def post_detail(request, id):
    # if attemping to get data from DB
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=id)
            post_dict = model_to_dict(post)
        except ObjectDoesNotExist:
            post_dict = {'error': 'object does not exist'}
    # if trying to post information to the DB
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


def add_post(request):
    if (request.method =='POST'):
        new_post = Post()
        new_post.author = request.POST.get('author')
        new_post.description = request.POST.get('description')
        new_post.location = request.POST.get('location')
        new_post.part = request.POST.get('part')
        new_post.payment_method = request.POST.get('payment_method')
        new_post.price = request.POST.get('price')
        new_post.transaction_type = request.POST.get('transaction_type')
        new_post.title = request.POST.get('title')
        new_post.save()


#     from django.shortcuts import render
# from login.models import Group, Profile
# from django.core.exceptions import ObjectDoesNotExist
# import json
# from django.http import JsonResponse
# from django.core import serializers
# import urllib.request
# import urllib.parse


# # Create your views here.
# def user_profile(request, username=None):
#     """
#     :param request: HTTP request
#     :param username: Given username for retrieving object attributes
#     :return: JsonResponse of serialized attributes
#     """

#     if request.method == 'GET':
#         try:
#             profile = Profile.objects.get(username=username)
#             x = model_to_dict(profile)
#         except ObjectDoesNotExist:
#             return JsonResponse({'status': 'false', 'message': 'ObjectDoesNotExist'}, status=500)

#     if request.method == 'POST':
#         try:
#             profile = Profile.objects.get(username=username)
#             x = model_to_dict(profile)
#             return JsonResponse({'status': 'true', 'message': 'Cannot edit'})
#         except ObjectDoesNotExist:
#             return JsonResponse({'status': 'false', 'message': 'ObjectDoesNotExist'})

#     del x['affiliations']
#     return JsonResponse(x, safe=False)

# def index(request):
#     if request.method == 'GET':
#         #result dictionary
#         all_profiles_dict = {}
#         try:
#             #getting all of the posts
#             all_profiles = Profile.objects.all().values()
#             #append each post to a dictionary
#             ### all_profiles seems to error out and cause a 500 error
#             # for profile in all_profiles:
#             #     all_profiles_dict[profile['id']] = profile
#             #response object showing that it worked

#             response = {'status': True, 'result': {'test': False}}
#             #return json object with success message
#             return JsonResponse(response, safe=False)

#         except ObjectDoesNotExist:

#             #response object showing that it failed
#             response = {'status': False, 'result': all_profiles_dict}

#             #return json object with failure message
#             return JsonResponse(response, safe=False)

#     #if attempting to save data to DB
#     if request.method == 'POST':
#         # all_profiles = Profile.objects.all().values()
#         all_profiles_dict = {'status': 'Nothing to POST'}


#     return JsonResponse(all_profiles_dict, safe=False)
