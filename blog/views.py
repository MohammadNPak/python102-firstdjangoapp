from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from .models import Post,Comment
from .forms import LoginForm
# Create your views here.

def index(request):
    return render(request,"blog/index.html",{})

@login_required
def posts(request):
    if request.method == "GET":
        all_posts = Post.objects.all()
        # first_post=all_posts[0]
        return render(
            request,
            'blog/posts.html',
            context={"all_posts":all_posts})
    elif request.method == "POST":
        author = request.user.userprofile
        body = request.POST["post_body"]
        Post.objects.create(body=body,author=author)
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

# def test(request):
#     if request.method == "GET":
#         form = LoginForm()
#         # print(request.GET)
#         # print(request.POST)
#         return render(request,"blog/test.html",{"form":form})
#     elif request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             email = form.cleaned_data["email"]
#             print(username)
#             print(password)
#             print(email)
#         # print(form)
#     return render(request,"blog/test.html",{"form":form})

from .forms import TestForm

class TestView(View):
    def get(self,request):
        form = TestForm()
        return render(request,"blog/test.html",{"form":form})

    def post(self,request):
        description = request.POST.get("description")
        image = request.FILES.get("user_profile_picture")
        form = TestForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            # with open("D:\code\maktabsharif\s22\image.png","wb+") as fp:
            #     for chunk in image.chunks():
            #         fp.write(chunk)
            form.save()
            
        return render(request,"blog/test.html",{"form":form})