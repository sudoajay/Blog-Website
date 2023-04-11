from datetime import date

from django.shortcuts import render

# from .models import addPost

all_posts = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


def get_date(post):
    return post['date']


# Create your views here.
def starting_page(request):
    # allpost = addPost.objects.all()
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = all_posts[-3:]if(len(all_posts) >3) else all_posts
    return render(request, "blog/index.html",{
        "posts": latest_posts
    })
    
def posts(request):
    # allpost = addPost.objects.all()
    return render(request,"blog/all-posts.html",{
        "all_posts": all_posts

    })
    
def post_detail(request,slug):
    # getPost= addPost.objects.get(slug = slug) 
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/post-detail.html", {
        "post": all_posts
    })