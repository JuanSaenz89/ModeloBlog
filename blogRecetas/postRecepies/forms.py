from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model =  Post
        fields = ('receta','author','body')
        widget = {
            'receta': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body':   forms.TextInput(attrs={'class':'form-control'}),
                  }
