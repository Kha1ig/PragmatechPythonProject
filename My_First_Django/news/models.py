from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.

class News_Post(models.Model):
    post_name = models.CharField(max_length=50, blank=False, null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    card_text = models.TextField(max_length=300, blank=False, null=False)
    image = models.ImageField(upload_to = 'news_post/')

    class Meta:
        verbose_name = 'News_Post'
        verbose_name_plural = 'News_Posts'

    def __str__(self):
        return f'{self.post_name}'
