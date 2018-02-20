from django.shortcuts import render
from .models import Group, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

# Create your views here.
def user_profile(request, username=None):
    # context = {}
    # if request.method == 'GET':
    #     try:
    #         profile = Profile.objects.get(username=username)
    #         context['profile'] = profile
    #     except ObjectDoesNotExist:
    #         return render(request, 'error.html')
    # return render(request, 'profile.html', context)

    if request.method == 'GET':
        try:
            profile = Profile.objects.get(username=username)
            p_list = list(profile)
        except ObjectDoesNotExist:
            return render(request, 'error.html')
    return JsonReponse(p_list, safe=False)


