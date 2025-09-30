from blog import models
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_author', 'post_body']
        widgets = {
            'post_title' : forms.TextInput(attrs={'class': 'form-control'}),
            'post_author' : forms.TextInput(attrs={'class': 'form-control'}),
            'post_body' : forms.Textarea(attrs={'class': 'form-control'}),
        }

        