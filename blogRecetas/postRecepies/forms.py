from django import forms
from .models import Post, Messages

class PostForm(forms.ModelForm):
    class Meta:
        model =  Post
        fields = ('title','author','body','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'author', 'type':'hidden'}),
            'body'  : forms.Textarea(attrs={'class':'form-control','label':'Instrucciones'}),
                  }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('sender','reciever','title' ,'msg_content')

        widgets = {

            'sender': forms.TextInput(attrs={'class':'form-control','value':'','id':'sender', 'type':'hidden'}),
            'reciever': forms.Select(attrs={'class':'form-control','id':'reciever',}),
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'msg_content': forms.Textarea(attrs={'class':'form-control','label':'Mensaje'}),

                    }
        