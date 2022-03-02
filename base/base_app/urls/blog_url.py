
from django import views
from django.urls import path
from base_app.views.blog_views import blog


urlpatterns = [
    path('', blog),
    
]