from .models import Profile, Post, Authenticator
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth.hashers import is_password_usable, make_password

from hardware_models import settings
import os
import hmac



# returns the homepage of posts
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


# see if the authenticator exists
@csrf_exempt
def check_auth(request):
    # if method is POST
    if request.COOKIES.get('authenticator'):

        # get the authenticator passed in from the web layer
        auth = request.COOKIES.get('authenticator')

        try:
            Authenticator.objects.get(auth=auth)
            context = {'status': True}
            return JsonResponse(context)

        # if user not found
        except ObjectDoesNotExist:
            context = {'status': False}
            return JsonResponse(context)
    else:
        context = {'status': False, 'error': 'Authenticator does not exist in cookie'}
        return JsonResponse(context)


def add_post(request):
    if (request.method == 'POST'):
        try:
            auth = request.COOKIES.get('authenticator')
            auth_object = Authenticator.objects.get(auth=auth)
            user_profile = Profile.objects.get(user_id=auth_object.user_id)
            searched_author = Profile.objects.get(username=user_profile.user_name)
            new_post = Post(
                author=searched_author,
                description=request.POST.get('description'),
                location=request.POST.get('location'),
                part=request.POST.get('part'),
                payment_method=request.POST.get('payment_method'),
                price=request.POST.get('price'),
                transaction_type=request.POST.get('transaction_type'),
                title=request.POST.get('title'),
            )
            new_post.save()
            context = {'status': True, 'result': 'Success'}
        except ObjectDoesNotExist:
            context = {'status': False, 'result': 'Author is not valid'}

        return JsonResponse(context)
    else:
        context = {'status': True, 'result': 'Get'}
        return JsonResponse(context)


# registering a new user
@csrf_exempt
def register(request):
    # if method is POST
    if request.method == "POST":

        # get post details
        display_name = request.POST['display_name']
        email = request.POST['email']
        username = request.POST['username']
        if is_password_usable(request.POST['password']):
            password = request.POST['password']
        else:
            context = {
                'status': False,
                'result': 'Password is not usable'
            }
            return JsonResponse(context)


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
            profile = Profile.objects.get(username=username, password=password)
            auth = create_authenticator(profile.id)

            context = {
                'status': True,
                'result': auth['auth']
            }

        # if user not found
        except ObjectDoesNotExist:
            context = {
                'status': False,
                'result': 'Invalid username or username/password combination'
            }

            # return the JsonResponse
        return JsonResponse(context)

    # if trying to GET
    return HttpResponse("Error, cannot complete GET request")


# create the authenticator instance
def create_authenticator(u_id):
    random_value = hmac.new(
        key=settings.SECRET_KEY.encode('utf-8'),
        msg=os.urandom(32),
        digestmod='sha256',
    ).hexdigest()

    # create a new auth
    new_auth = Authenticator(user_id=u_id, auth=random_value)

    # save everything
    new_auth.save()

    # turn into dictionary
    auth_dict = model_to_dict(new_auth)

    # return 
    return auth_dict


@csrf_exempt
def logout(request):
    # if method is POST
    if request.method == "POST":

        # get the authenticator passed in from the web layer
        auth = request.POST['authenticator']

        # try to find the user with username
        try:
            instance = Authenticator.objects.get(auth=auth)

            context = {
                'status': True,
                'result': 'You have successfully logged out'
            }

            instance.delete()

        # if user not found
        except ObjectDoesNotExist:
            context = {
                'status': False,
                'result': 'User is not logged in'
            }

            # return the JsonResponse
        return JsonResponse(context)

    # if trying to GET
    return HttpResponse("Error, cannot complete GET request")

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
