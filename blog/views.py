from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    post = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": post})


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {
        "all_post": all_posts
    })


def post_detail(request, slug):

    post_object = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        "post": post_object,
        "post_tags": post_object.tag.all()
    })
