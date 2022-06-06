from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
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