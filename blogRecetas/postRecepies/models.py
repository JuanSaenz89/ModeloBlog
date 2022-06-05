from msilib.schema import Class
from unicodedata import category
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from ckeditor.fields import RichTextField

class Ingrediente(models.Model):
    ingrediente = models.CharField(max_length=100)
    cantidad =    models.IntegerField()


class Categoria(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class Post(models.Model):
    receta = models.CharField(max_length=255)
    body =   RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_post = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=100, default='Sin categoria')

    def __str__(self):
        return self.receta + ' - ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('index')