from tkinter import CASCADE
from turtle import title
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=127, blank=False, null=False)
    bio = models.TextField(blank=True, null=True)
    age = models.CharField(max_length=127, blank=False, null=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=127, blank=False, null=False)
    card_text = models.TextField(blank= False, null=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.author}\' s Post - {self.title}'

