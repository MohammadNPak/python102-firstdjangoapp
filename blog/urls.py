from django.urls import path
from .views import (posts,post_detail,TestView,add_favorite,
                    Like,set_dark)

urlpatterns = [
    path("posts",posts,name="posts"),
    path("post/<slug:slug>",post_detail,name="post_detail"),
    path("post/<slug:slug>/like",Like.as_view(),name="like"),
    path("test/",TestView.as_view() ,name="test"),
    path("add_favorite/<slug:slug>",add_favorite ,name="add_favorite"),
    path("set_dark",set_dark ,name="set_dark"),
]
    