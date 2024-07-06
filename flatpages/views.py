from django.shortcuts import render
from django.http import HttpResponse
from django import template

def home(request):
    return render(request, "templates/static_handler.html")

def single_text(request):
    return HttpResponse(u'Привет, Мир! А я изучаю DJANGO!!!', content_type="text/plain; charset=utf-8")