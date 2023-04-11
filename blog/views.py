from datetime import date

from django.shortcuts import render

from .models import addPost



def get_date(post):
    return post['date']


# Create your views here.
def starting_page(request):
    allpost = addPost.objects.all()
    # sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = allpost[len(allpost)-3:]if(len(allpost) >=3) else allpost
    return render(request, "blog/index.html",{
        "posts": latest_posts
    })
    
def posts(request):
    allpost = addPost.objects.all()
    return render(request,"blog/all-posts.html",{
        "all_posts": allpost

    })
    
def post_detail(request,slug):
    getPost= addPost.objects.get(slug = slug) 
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/post-detail.html", {
        "post": getPost
    })