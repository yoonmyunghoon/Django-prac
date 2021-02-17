from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from .models import Article, Comment
from .forms import ArticleForm


def index(request):
    articles = Article.objects.order_by("-pk")
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # title = form.cleaned_data.get("title")
            # content = form.cleaned_data.get("content")
            # image = form.cleaned_data.get("image")
            # article = Article(title=title, content=content, image=image)
            # article.save()
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "articles/form.html", context)


def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    context = {"article": article, "comments": comments}
    return render(request, "articles/detail.html", context)


def delete(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        article.delete()
        return redirect("articles:index")
    return redirect("articles:detail", article.pk)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            # article.title = form.cleaned_data.get("title")
            # article.content = form.cleaned_data.get("content")
            # if form.cleaned_data.get("image"):
            #     article.image = form.cleaned_data.get("image")
            # article.save()
            form.save()
            return redirect("articles:detail", article.pk)
    else:
        # form = ArticleForm(initial=article.__dict__)
        form = ArticleForm(instance=article)
    context = {"form": form, "article": article}
    return render(request, "articles/form.html", context)


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
