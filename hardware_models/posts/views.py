from .models import Profile, Post, Authenticator
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.db import IntegrityError
import urllib.request
from random import randint
import urllib.parse
import json

#returns the homepage of posts
def home(request):
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

# registering a new user
@csrf_exempt
def register(request):

    # if method is POST
    if request.method == "POST":

        # get post details
        display_name = request.POST['display_name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        # create the user profile
        new_profile = Profile(display_name=display_name, email=email, password=password, username=username)

        # see if user already exists with that username
        try:
            new_profile.save()
            context = {
            'status': True,
            'result': 'User profile successfully created'
            }

        # if the unique username already exists
        except IntegrityError:
            context = {
            'status': False,
            'result': 'User already exists with that username'
            }

        # return the JsonResponse
        return JsonResponse(context)

    # if trying to GET
    return HttpResponse("Error, cannot complete GET request")

@csrf_exempt
def login(request):

    # if method is POST
    if request.method == "POST":

        # getting POST data
        username = request.POST['username']
        password = request.POST['password']

        # try to find the user with username
        try:
            profile = Profile.objects.get(username=username)
            auth = create_authenticator(profile.id)

            context = {
                'status': True,
                'result': auth
            }

        # if user not found
        except Profile.DoesNotExist:
            context = {
                'status': False,
                'result': 'User does not exist'
            }  

        # return the JsonResponse
        return JsonResponse(context)

    # if trying to GET
    return HttpResponse("Error, cannot complete GET request")


def create_authenticator(user_id):
    """ Creates new object
        :param user_id: Integer associated with auth
        :return: JsonResponse
        """
    range_start = 10 ** (256 - 1)
    range_end = (10 ** 256) - 1
    random_value = randint(range_start, range_end)

    # create a new auth
    new_auth = Authenticator(user_id=user_id, authenticator=random_value)

    # save everything
    new_auth.save()
    auth_dict = model_to_dict(new_auth)
    return JsonResponse(auth_dict)


def check_authenticator(authenticator, user_id):
    """
        Validates authenticator object
        :param authenticator: Object's 256 digit integer value
        :param user_id: Int associated with auth
        :return: Returns True if autenticator associated with user_id is in the db
    """

    if Authenticator.objects.filter(authenticator=authenticator, user_id=user_id).exists():
        return True
    else:
        return False


def logout(request):
    # if method is POST
    if request.method == "POST":
        # get the authenticator passed in from the web layer
        detail = {'authenticator': request.POST['authenticator']}

        # pass encoded data to the model layer api
        enc_data = urllib.parse.urlencode(detail).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/api/logout/', enc_data)

        # get the return json
        json_response = urllib.request.urlopen(req).read().decode('utf-8')
        context = json.loads(json_response)

        # return the JsonResponse
        return JsonResponse(context)

    # if trying to GET
    return HttpReponse("Error, cannot complete GET request")


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


