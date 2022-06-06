from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Messages
from .forms import PostForm, MessageForm
class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']
class PostDetailView(DetailView):
    model = Post
    template_name = 'detalle_receta.html'

class PostCreateView(CreateView):
    model =      Post
    form_class = PostForm
    template_name = "agregar_receta.html"
    

class PostUpdateView(UpdateView):
    model =      Post
    form_class = PostForm
    template_name = "editar_receta.html"

class PostDeleteView(DeleteView):
    model =      Post
    template_name = "borrar_receta.html"
    success_url = '/'

def about_me(request):
    return render(request, 'about_me.html')

class MessagesView(ListView):
    model = Messages
    template_name = 'inbox.html'
    ordering = ['-id']

    

class MessageSendView(CreateView):
    model = Messages
    form_class = MessageForm
    template_name = "send_message.html"

class MessageDetailView(DetailView):
    model = Messages
    template_name = 'message_detail.html'
    
