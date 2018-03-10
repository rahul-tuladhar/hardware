from django.shortcuts import render
from hardware_models.posts.models import Post
from hardware_models.posts.forms import PostEditForm
import json

# Create your views here.
def index(request):
    req = urllib.request.Request('http://placeholder.com/call-to-exp-layer')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return render(response, 'template.html', context)


def post_detail(request, post_title=None):
    context = {}
    if request.method == 'GET':
        try:
            post = Post.objects.get(title=post_title)
            context['post'] = post
        except ObjectDoesNotExist:
            return render(request, 'error.html')
    return render(request, 'post_detail.html', context)

def edit_post(request, post_title=None):
    context = {}
    if request.method == 'POST':
        try:
            form = PostEditForm(request.POST)
            if form.is_valid():
                context['form'] = form
                form.save()
                return render(request, 'index.html', context)
            else:
                return render(request, 'index.html', context)
        except ObjectDoesNotExist:
            return render(request, 'error.html')
    else:
        try:
            post = Post.objects.get(title=post_title)
            context['post'] = post
            form = PostEditForm(request.POST, instance=post)
            context['form'] = form
        except ObjectDoesNotExist:
            return render(request, 'error.html')
        return render(request, 'edit_post.html', context)
