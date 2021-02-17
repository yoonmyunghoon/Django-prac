from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Article, Comment


def index(request):
    articles = Article.objects.order_by("-pk")
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        article = Article(title=title, content=content, image=image)
        article.save()
        return redirect("articles:detail", article.pk)
    else:
        return render(request, "articles/create.html")


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comments.all()
    context = {"article": article, "comments": comments}
    return render(request, "articles/detail.html", context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        article.delete()
        return redirect("articles:index")
    return redirect("articles:detail", article.pk)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        if request.FILES.get("image"):
            article.image = request.FILES.get("image")
        article.save()
        return redirect("articles:detail", article.pk)
    else:
        context = {"article": article}
        return render(request, "articles/update.html", context)


def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        content = request.POST.get("content")
        comment = Comment(article=article, content=content)
        comment.save()
    return redirect("articles:detail", article.pk)


def comments_delete(request, article_pk, comment_pk):
    if request.method == "POST":
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect("articles:detail", article_pk)


def comments_update(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "POST":
        comment.content = request.POST.get("content")
        comment.save()
        return redirect("articles:detail", article_pk)
    else:
        context = {"comment": comment}
        return render(request, "articles/comment_update.html", context)
