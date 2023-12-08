from django.shortcuts import render
from .models import Post,Comment
from accounts.models import UserProfile
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import LoginForm
# Create your views here.

def posts(request):
    if request.method == "GET":
        all_posts = Post.objects.all()
        # first_post=all_posts[0]
        return render(
            request,
            'blog/posts.html',
            context={"all_posts":all_posts})
    elif request.method == "POST":
        body = request.POST["post_body"]
        Post.objects.create(body=body)
        return HttpResponse(f"new post was created successfully!")
    

def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    if request.method=="GET":
        return render(request,"blog/post_detail.html",context={"post":post})
    elif request.method == "POST":
        body = request.POST.get("new_comment_body")
        Comment.objects.create(
            body=body,
            post=post,
            author=UserProfile.objects.first())
        return render(request,"blog/post_detail.html",context={"post":post})

def test(request):
    if request.method == "GET":
        form = LoginForm()
        # print(request.GET)
        # print(request.POST)
        return render(request,"blog/test.html",{"form":form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            print(username)
            print(password)
            print(email)
        # print(form)
    return render(request,"blog/test.html",{"form":form})
    