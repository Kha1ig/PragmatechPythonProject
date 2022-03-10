from django.contrib import admin

# Register your models here.

from news.models import News_Post

admin.site.register(News_Post)