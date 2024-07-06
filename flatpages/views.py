from django.shortcuts import render, redirect
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

def create_post(request):
    if request.user.is_authenticated:
    #if True:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                if Article.objects.get(title=form["title"]):
                    # если навзание статьи не уникально
                    form['errors'] = u"Статья с таким названием уже есть"
                    return render(request, 'article_form.html', {'form': form})
                # если поля заполнены без ошибок
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'article_form.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'article_form.html', {})
    else:
        raise Http404