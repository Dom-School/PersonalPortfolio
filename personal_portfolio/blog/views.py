from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import CommentForm
from .models import Post, Comment


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {"posts": posts}
    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "posts": posts,
        "category": category,
        }
    return render(request, 'blog_category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = Comment(
            author=form.cleaned_data["author"],
            body=form.cleaned_data["body"],
            post=post
        )
        comment.save()
        return redirect(request.path)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, 'blog_detail.html', context)