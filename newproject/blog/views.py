from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

from .forms import PostForm
from django.shortcuts import redirect
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

def add_post(request):
    blogform = PostForm()
    if request.method == "POST":
        blogform = PostForm(request.POST)
        if blogform.is_valid():
            blogform.save()
            return redirect('myposts')
    return render(request, "post_form.html", {"blogform": blogform})


def find_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "postdetail.html", {"post": post})

def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    blogform = PostForm(instance=post)
    if request.method == "POST":
        blogform = PostForm(request.POST, instance=post)
        if blogform.is_valid():
            blogform.save()
            return redirect('myposts')
    return render(request, "post_form.html", {"blogform": blogform})
    

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('myposts')