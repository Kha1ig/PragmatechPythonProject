from django.shortcuts import render, redirect
from contact.forms import Contactform
from contact.models import Contact
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib import messages
# Create your views here.
@csrf_exempt
def contact(request):

    forum = Contactform()
    if request.method == 'POST':
        form = Contactform(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your message has been received!')
           
            return redirect(reverse('about:about'))

    return render (request, 'contact.html', {'forum': forum})
    