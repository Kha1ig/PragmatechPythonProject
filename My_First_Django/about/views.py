import imp
from multiprocessing import context
from django.shortcuts import render
from about.models import Post

# Create your views here.

def about(request):
    abouts = Post.objects.all()
    
    context = {
        'abouts': abouts
    }


    return render(request, 'about_me.html', context = context)
    
def about_detail(request, about):

    abouts = Post.objects.all()

    about = abouts

    return render (request, 'about-detail.html', {'about': about})