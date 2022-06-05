from . import views
from django.urls import path
from .views import *
urlpatterns = [
    path('registration/', UserCreate.as_view(), name='registro'),
    path('edit_user/', UserEdit.as_view(), name='editar_perfil'),
    path('password/', PassWordsChange.as_view(), name='cambiar_password'),
    path('password_success/', views.password_success, name='password_success'),
]
