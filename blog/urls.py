from django.urls import path
from .views import posts,post_detail,test

urlpatterns = [
    path("posts",posts,name="posts"),
    path("post/<slug:slug>",post_detail,name="post_detail"),
    path("test",test,name="test"),
]
    