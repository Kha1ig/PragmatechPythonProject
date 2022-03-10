from django.shortcuts import render

from news.models import News_Post

# Create your views here.

def news(request):
    news = News_Post.objects.all()

    context = {
        'news': news
    }

    return render(request, 'news.html', context = context)


def news_detail(request,pk):

    new_news = News_Post.objects.get(pk=pk)

    return render (request, 'news-detail.html', {'news': new_news})
