from .models import Post, Authenticator
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict


def create_authenticator(user_id):
    """ Creates new object
        :param user_id: Integer associated with auth
        :return: JsonResponse
        """
    new_auth = Authenticator.create(user_id)
    auth_dict = model_to_dict(new_auth)
    return JsonResponse(auth_dict)


def check_authenticator(authenticator, user_id):
    """
        Validates authenticator object
        :param authenticator: Object's 256 digit integer value
        :param user_id: Int associated with auth
        :return: Returns True if autenticator associated with user_id is in the db
    """
    db_auth = Authenticator.objects.get(authenticator=authenticator, user_id=user_id)
    if db_auth:
        return True
    else:
        return False

def home(request):
    """
    Returns a JsonResponse dictionary of database values.
    """
    all_posts_dict = {}  # result dictionary

    if request.method == 'GET':  # if attempting to get data from DB

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
    """
    Returns a JsonResponse dictionary of a post during a POST Request.
    :param request: HTTP response
    :param id: post primary key
    :return: JsonResponse
    """
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
    :param id:
    :return: JsonResponse
    """
    if request.method == 'GET':
        post_dict = {'status': 'should not get request edit_post'}
    # TODO: Fully implement the entity API layer of this method
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=id)
            post_dict = model_to_dict(post)
        except ObjectDoesNotExist:
            post_dict = {'status': 'ObjectDoesNotExist'}
    return JsonResponse(post_dict, safe=False)

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
