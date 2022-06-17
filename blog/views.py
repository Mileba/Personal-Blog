from django.shortcuts import render
from datetime import date
from .models import Post


# def get_date(Post):
#     return Post.get('date')


def index(request):
    post = Post.objects.all().order_by("title")
    # sorted_posts = sorted(post)
    latest_posts = post[0:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {
        "all_post": all_posts
    })


def post_detail(request, slug):
    post_object = Post.objects.all()
    identified_post = next(
        post for post in post_object if post.slug == slug)
    return render(request, 'blog/post-detail.html', {
        "post": identified_post
    })
