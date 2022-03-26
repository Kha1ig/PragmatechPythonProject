from dataclasses import fields
from django import forms
from django.forms import ModelForm
from contact.models import Contact

class Contactform(ModelForm):
    pass

    class Meta():
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'input1',
                    'placeholder': 'Name',

                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'input1',
                    'placeholder': 'Email',

                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'input1',
                    'placeholder': 'Subject',

                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'input1',
                    'placeholder': 'Message',
                    'rows': '5',

                }
            ),

        }
    