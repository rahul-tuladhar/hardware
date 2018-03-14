from django.shortcuts import render
from .models import Post
from .forms import PostEditForm
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
import json

#show the details of a review
def review_detail(request):
	#if attemping to get data from DB
    if request.method == 'GET':
        try:
            review = Review.objects.get(id=id)
            review_dict = model_to_dict(review)
            
        except ObjectDoesNotExist:
            review_dict = {'error': 'object does not exist'}

    #if trying to post information to the DB
    if request.method == 'POST':
        review_dict = {'status': 'nothing to POST, only viewing a post detail'}

    return JsonResponse(review_dict, safe=False)