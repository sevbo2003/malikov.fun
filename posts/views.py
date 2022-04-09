from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Note, Category, Tag
from .forms import CommentForm
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def like_view(request, pk):
    post = get_object_or_404(Post, pk=request.POST.get('post_id'))
    post.likes.add(request.user)
    path = f"{post.get_absolute_url()}#like-id"
    return HttpResponseRedirect(path)


def save_view(request, pk):
    post = get_object_or_404(Post, pk=request.POST.get('post_save_id'))
    post.saves.add(request.user)
    path = f"{post.get_absolute_url()}"
    return HttpResponseRedirect(path)

def delete_save_view(request, pk):
    post = get_object_or_404(Post, pk=request.POST.get('post_delete_id'))
    post.saves.remove(request.user)
    path = f"{post.get_absolute_url()}"
    return HttpResponseRedirect(path)

def home(request):
    query = request.GET.get('search')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        posts = Post.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def by_category(request, category):
    category = get_object_or_404(Category, category=category)
    posts = Post.objects.filter(category=category)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'by-category.html', context)


def by_tag(request, tag):
    tag = get_object_or_404(Tag, tag=tag)
    posts = Post.objects.filter(tags__tag__icontains=tag)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'tag': tag
    }
    return render(request, 'by-tag.html', context)


def saved_posts(request):
    posts = Post.objects.filter(saves__username=request.user)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts
    }
    return render(request, 'saved-items.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            author = request.user
            post = post
            comment = comment_form.cleaned_data['comment']
            created = datetime.now()
            p = Comment(post=post, author=author, comment=comment, created=created)
            p.save()
            path = f"{post.get_absolute_url()}#mc-embedded-subscribe-form"
            return HttpResponseRedirect(path)
    else:
        comment_form = CommentForm
    post = get_object_or_404(Post, slug=slug)
    try:
        next = Post.objects.get(id=post.id+1)
    except:
        next = False
    try:
        prev = Post.objects.get(id=post.id-1)
    except:
        prev = False
    context = {
        'post': post,
        'comment_form': comment_form,
        'next': next,
        'prev': prev
    }
    return render(request, 'post-detail.html', context)


def about_me(request):
    return render(request, 'about-me.html')


def notes(request):
    query = request.GET.get('note-search')
    if query:
        notes = Note.objects.filter(Q(title__icontains=query))
    else:
        notes = Note.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(notes, 10)
    try:
        notes = paginator.page(page_num)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    context = {
        'notes': notes
    }
    return render(request, 'notes.html', context)
