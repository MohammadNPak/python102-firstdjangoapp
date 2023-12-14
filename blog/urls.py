from django.urls import path
from .views import posts,post_detail,TestView

urlpatterns = [
    path("posts",posts,name="posts"),
    path("post/<slug:slug>",post_detail,name="post_detail"),
    path("test/",TestView.as_view() ,name="test"),
]
    