from django.shortcuts import render

# Create your views here.
def users_view(request):
    return render(request, 'users.html')
