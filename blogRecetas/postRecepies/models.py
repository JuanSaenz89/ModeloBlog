from email import header
from msilib.schema import Class
from tabnanny import check
from unicodedata import category
from django.dispatch import receiver
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True) 


    def __str__(self):
        return str(self.user.username)
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    body =   RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_post = models.DateField(auto_now_add=True)
    header_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title + ' - ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('index')

class Messages(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    msg_content = RichTextField(max_length=500, blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.title + ' - ' + str(self.sender)

    def get_absolute_url(self):
        return reverse('inbox')


