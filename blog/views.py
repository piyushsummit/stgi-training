from django.http import Http404
from django.shortcuts import render

# Store the saved posts in a dictionary
saved_posts = {
    'first-post': {
        "post_name": 'first-post',
        "post_image": "blog/images/naruto.jpeg",
        "post_title": 'My first post!',
        "post_body": "This is the body of my first post."
    },
    'second-post': {
        "post_name": 'second-post',
        "post_image": "blog/images/naruto.jpeg",
        "post_title": 'My second post!',
        "post_body": "This is the body of my second post."
    },
    'third-post': {
        "post_name": 'third-post',
        "post_image": "blog/images/naruto.jpeg",
        "post_title": 'My third post!',
        "post_body": "This is the body of my third post."
    },
}

def landing_page(request):
    latest_post = list(saved_posts.values())[-1]
    return render(request, "blog/index.html", {"post": latest_post})

def posts(request):
    post_list = saved_posts.values()
    return render(request, "blog/all-posts.html", {"post_list": post_list})

def single_post(request, slug):
    post = saved_posts.get(slug)
    if not post:
        raise Http404
    return render(request, "blog/individual-post.html", {"post": post})
