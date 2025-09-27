from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    
    sentence = "This is the first django view thing"
    
    return render(request, 'index.html', {'sentence': sentence})
    
def body(request):
    words = "these are some other words"
    return render(request, 'index.html', {"words": words})

def button(request):
    sentence = "This is the first django view thing"
    words = "these are some other words"
    return render(request, "button.html", {"sentence": sentence, "words": words})

def show_post(request):
    post = Post.objects.all()
    return render(request, "post_list.html", {"post": post})