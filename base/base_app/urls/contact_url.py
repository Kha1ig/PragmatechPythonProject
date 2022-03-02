from django import views
from django.urls import path
from base_app.views.contact_views import contact

urlpatterns = [
    path('', contact),
]