from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class Blog(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Nome do blog')
    description = models.TextField(verbose_name='Descrição')
    tags = models.CharField(max_length=200, help_text='Separes as tags por virgula!')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs', verbose_name='Usuário')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name



class Post(models.Model):
    image = models.ImageField(upload_to='pictures/%Y/%m')
    description = models.TextField(verbose_name='Descrição do post')
    tags = models.CharField(max_length=200, help_text='Separe as tags por virgula')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts', verbose_name='Blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:30]


