from distutils.command.upload import upload
from distutils.text_file import TextFile
from operator import mod
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.

class company(models.Model):
    owner = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.owner


class phone(models.Model):

    # relations
    brand = models.ForeignKey(company, on_delete=models.CASCADE, related_name='phones')
    
    # model main fields
    name = models.CharField(max_length=200, db_index=True)
    price = models.IntegerField()
    ram = models.IntegerField(default=4)
    storage = models.IntegerField(default=128)
    image = models.ImageField(upload_to = 'phone-images/')

    # migrations
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - by - {self.brand}'
