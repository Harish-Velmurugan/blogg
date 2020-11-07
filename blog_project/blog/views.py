from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from . models import Post,Comment
from django.views.generic.edit import CreateView
class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

def BlogDetailView(request,pk):
    post = Post.objects.get(pk = pk)
    comments = Comment.objects.filter(post = pk)
    return render(request,'blog/post_detail.html',{'post':post,'comments':comments})

class BlogCreateView(CreateView): 
    model = Post
    template_name ='blog/post_new.html' 
    fields = '__all__'