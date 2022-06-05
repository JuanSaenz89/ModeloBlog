from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model =  Post
        fields = ('receta','author','body')

        widgets = {
            'receta': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'author', 'type':'hidden'}),
            'body'  : forms.Textarea(attrs={'class':'form-control','label':'Instrucciones'}),
                  }
