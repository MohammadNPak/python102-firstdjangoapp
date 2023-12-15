from django.contrib import admin
from .models import Post,Comment
# Register your models here.
from django.db.models import Sum,Count


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","like_count","create_at")

    def like_count(self,obj):
        return (Post.objects.filter(id=obj.id)
                .aggregate(likes_count=Count("like"))["likes_count"])

# admin.site.register(Post)
admin.site.register(Comment)