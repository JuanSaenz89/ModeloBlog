from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Ingrediente(models.Model):
    ingrediente = models.CharField(max_length=100)
    cantidad =    models.IntegerField()


class Post(models.Model):
    receta = models.CharField(max_length=255)
    body =   models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.receta + ' - ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')