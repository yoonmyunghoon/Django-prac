from django.contrib import admin
from .models import Article, Comment, Hashtag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "image", "created_at", "updated_at")
    list_display_links = ("content",)
    list_filter = ("created_at",)
    list_editable = ("title",)
    list_per_page = 2


# admin.site.register(Article, ArticleAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "article_id", "content", "created_at", "updated_at")
    list_filter = ("created_at",)
    list_editable = ("content",)
    list_per_page = 2


# admin.site.register(Comment, CommentAdmin)


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    liset_display = ("content",)
