from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import RegistroForm, ProfileForm, PasswordsChangeForm

class PassWordsChange(PasswordChangeView):
    form_class = PasswordsChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_success')

    def get_object(self):
        return self.request.user

def password_success(request):
    return render(request, 'registration/password_success.html')




class UserCreate(generic.CreateView):
    form_class = RegistroForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

class UserEdit(generic.UpdateView):
    form_class = ProfileForm
    template_name = 'registration/editar_perfil.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

