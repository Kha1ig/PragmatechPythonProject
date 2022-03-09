from django.urls import path
from about.views import about, about_detail

app_name = 'about'

urlpatterns = [
    path('', about, name='about'),
    path('<int:pk>', about_detail, name='about_detail'),

]
