from django.shortcuts import render
from .models import Post
from .forms import PostEditForm
from django.http import JsonResponse

# Create your views here.
def index(request):
    # context = {}
    # all_posts = Post.objects.all()
    # context['posts'] = all_posts
    # return render(request, 'index.html', context

    all_posts = Post.objects.all()
    post_list = list(all_posts)
    return JSONResponse(post_list, safe=False)

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
