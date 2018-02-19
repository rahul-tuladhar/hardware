from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    context = {}
    all_posts = Post.objects.all()
    context['posts'] = all_posts
    return render(request, 'index.html', context)

def post_detail(request, post_title=None):
    context = {}
    if request.method == 'GET':
        try:
            post = Post.objects.get(title=post_title)
            context['post'] = post
        except ObjectDoesNotExist:
            return render(request, 'error.html')
    return render(request, 'post_detail.html', context)
