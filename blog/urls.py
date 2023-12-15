from django.urls import path
from .views import posts,post_detail,TestView,add_favorite

urlpatterns = [
    path("posts",posts,name="posts"),
    path("post/<slug:slug>",post_detail,name="post_detail"),
    path("test/",TestView.as_view() ,name="test"),
    path("add_favorite/<slug:slug>",add_favorite ,name="add_favorite"),
]
    