from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')
    
    def __init__(self, *args, **kwargs) -> None:
        super(RegistroForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

class ProfileForm(UserChangeForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','email','password','date_joined', 'last_login','is_superuser','is_staff','is_active')
    
class PasswordsChangeForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta: 
        model = User
        fields = ('old_password','new_password1','new_password2')

