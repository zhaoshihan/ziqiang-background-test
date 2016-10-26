# coding:utf-8

from django.shortcuts import render
from ziqiang.models import Newssite
# Create your views here.
def index(request):
    articles = Newssite.objects.all()
    return render(request, 'home.html', {'articles': articles})
