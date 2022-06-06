from django.urls import path
from .views import *
urlpatterns = [
             
    path('', HomeView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detalle_receta'),
    path('agregar_receta/', PostCreateView.as_view(), name='agregar_receta'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='editar_receta'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='borrar_receta'),
    path('about_me/', about_me, name='about_me'),
    path('inbox/', MessagesView.as_view(), name='inbox'),
    path('send_message/', MessageSendView.as_view(), name='send_message'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
   ]
