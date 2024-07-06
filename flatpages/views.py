from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(u'Привет, Мир! А я изучаю DJANGO!!!', content_type="text/plain; charset=utf-8")
