from django.shortcuts import render
from django.http import HttpResponse, Http404
from django import template
from articles.models import Article

def home(request):
    return render(request, "templates/static_handler.html")

def single_text(request):
    return HttpResponse(u'Привет, Мир! А я изучаю DJANGO!!!', content_type="text/plain; charset=utf-8")

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404