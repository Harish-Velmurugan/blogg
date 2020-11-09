from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.views.generic import ListView,DetailView
from . models import Post,Comment
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

def BlogDetailView(request,pk):
    try:
        post = Post.objects.get(pk = pk)
    except:
        raise Http404()
    comments = Comment.objects.filter(post = pk)
    return render(request,'blog/post_detail.html',{'post':post,'comments':comments})

class BlogCreateView(CreateView): 
    model = Post
    template_name ='blog/post_new.html' 
    fields = '__all__'

class CommentCreateView(CreateView): 
    model = Comment
    template_name ='blog/comment_new.html' 
    fields = '__all__'
    success_url = reverse_lazy('home')

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title','body']
    template_name = 'blog/post_edit.html'

class BlogDeleteView(DeleteView): 
    model = Post
    template_name = 'blog/post_delete.html' 
    success_url = reverse_lazy('home')