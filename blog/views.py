from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import BlogPost, BlogCommentForm
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'blogs': blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    comments = Comment.objects.filter(blog_id=blog_id)

    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)
        comment_form.instance.blog_id = blog_id
        if comment_form.is_valid():
            comment_form.save()
  
    else :
        comment_form = BlogCommentForm()

    context = {
            'blog_detail' : blog_detail,
            'comments': comments,
            'comment_form': comment_form
            
    }
    return render(request, 'blog/detail.html', context)


def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'blog/new.html',{'form':form})

def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    
    form = BlogPost(request.POST, instance = blog)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'blog/new.html', {'form' : form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

def comment_delete(request, comment_id) :
    comment = get_object_or_404(Comment, pk = comment_id)
    comment.delete()
    return redirect('home')

def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    comment_form = BlogCommentForm(request.POST, instance = comment)

    if request.method == "POST" :
        comment_form = BlogCommentForm(request.POST, instance = comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('home')
    else :
        form = BlogCommentForm(instance = comment)

    return render(request, 'blog/comment.html', {'comment_form' : comment_form})

