from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm
class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'detalle_receta.html'

class PostCreateView(CreateView):
    model =      Post
    form_class = PostForm
    template_name = "agregar_receta.html"
    # fields = ['receta','author','body']

class PostUpdateView(UpdateView):
    model =      Post
    form_class = PostForm
    template_name = "editar_receta.html"