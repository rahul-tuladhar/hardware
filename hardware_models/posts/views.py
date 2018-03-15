from .models import Post
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict


# returns a JsonResponse dictionary with all of the Post objects' attributes
def index(request):
    # if attempting to get data from DB
    if request.method == 'GET':

        # result dictionary
        all_posts_dict = {}

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
            del post_dict['image']

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
