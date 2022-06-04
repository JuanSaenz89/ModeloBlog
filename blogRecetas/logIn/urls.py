from atexit import register
from django.urls import path
from .views import *
urlpatterns = [
    path('registration/', UserCreate.as_view(), name='registro'),

]
