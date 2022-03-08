from turtle import title
from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=127, blank=False, null=False)
    card_text = models.TextField(blank= False, null=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.title}'

