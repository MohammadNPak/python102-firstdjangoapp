from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserProfile
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Q,When,Case,IntegerField,Count


from .models import Post,Comment
from .forms import LoginForm
# Create your views here.

def index(request):
    return render(request,"blog/index.html",{})


# @login_required
def posts(request):
    # print(request.session["favorite"])
    if request.method == "GET":
        # fav_posts = Post.objects.filter(id__in=request.session["favorite"])
        # not_fav_posts = Post.objects.filter(
        #     ~Q(id__in=request.session["favorite"]))

        # all_posts = fav_posts.union(not_fav_posts)
        
        if request.session.get("favorite"):
            all_posts = (Post.objects.all()
                        .annotate(likes_count=Count("like"))
                        .annotate(dislikes_count=Count("dislike"))
                        .annotate(is_fav=
                Case(
                    When(id__in=[int(x) for x in request.session["favorite"]], then=1),
                    default=0, output_field=IntegerField()
                )).order_by("-is_fav","create_at"))
        else:
            all_posts = (Post.objects.all()
                        .annotate(likes_count=Count("like"))
                        .annotate(dislikes_count=Count("dislike"))
                        .annotate(is_fav=
                Case(
                    When(id__in=[], then=1),
                    default=0, output_field=IntegerField()
                )).order_by("-is_fav","create_at"))
    

        paginator = Paginator(all_posts,2)
        current_page = request.GET.get("page")
        if current_page:
            page_posts = paginator.get_page(int(current_page))
        else:
            page_posts = paginator.get_page(1)


        # first_post=all_posts[0]
        return render(
            request,
            'blog/posts.html',
            context={"all_posts":page_posts})
    elif request.method == "POST":
        author = request.user.userprofile
        body = request.POST["post_body"]
        Post.objects.create(body=body,author=author)
        return HttpResponse(f"new post was created successfully!")
    

@login_required
def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    if request.method=="GET":
        return render(request,"blog/post_detail.html",context={"post":post})
    elif request.method == "POST":
        body = request.POST.get("new_comment_body")
        Comment.objects.create(
            body=body,
            post=post,
            author=request.user.userprofile)
        return render(request,"blog/post_detail.html",context={"post":post})


def add_favorite(request,slug):
    if not request.session.get("favorite"):
        request.session["favorite"] = []

    id = Post.objects.get(slug=slug).id
    if id in request.session["favorite"]:
        s = request.session["favorite"]
        s.remove(id)
        request.session["favorite"] = s

    else:
        request.session["favorite"] = request.session["favorite"]+[id]
    
    return redirect(reverse("posts"))

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
            form.save()
            
        return render(request,"blog/test.html",{"form":form})
    


class Like(View,LoginRequiredMixin):
    def post(self,request,slug):
        post = get_object_or_404(Post,slug=slug)
        is_liked = post.like.filter(id=request.user.userprofile.id)
        if is_liked:
            post.like.remove(request.user.userprofile)
        else:
            post.like.add(request.user.userprofile)
        return redirect(reverse("posts"))


def set_dark(request):
    res = redirect(reverse("index"))
    res.set_cookie("dark","True")
    return res
    



