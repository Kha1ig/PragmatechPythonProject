from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def about(request):
    abouts = [

             {
                'about1': {
                    'name': 'Ali',
                    'surname': 'Aliyev',
                    'age':  21
                },
                'about2': {
                    'name': 'Cemil',
                    'surname': 'Huseynov',
                    'age':  22
                }

            }
        ]
    
    context = {
        'abouts': abouts[0]
    }


    return render(request, 'about_me.html', context = context)
    
def about_detail(request, about):

    abouts = [

             {
                'about1': {
                    'name': 'Ali',
                    'surname': 'Aliyev',
                    'age':  21
                },
                'about2': {
                    'name': 'Cemil',
                    'surname': 'Huseynov',
                    'age':  22
                }

            }
        ]

    about = abouts[0][about]

    return render (request, 'about-detail.html', {'about': about})