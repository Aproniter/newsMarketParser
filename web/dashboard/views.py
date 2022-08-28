from django.shortcuts import render, redirect

from utils.scraper import run_scraper
from .models import News

def index(request):
    news_list = News.objects.all()
    context = {'news_list': news_list}
    return render(request, 'dashboard/index.html', context)

def new_parse(request):
    News.objects.all().delete()
    run_scraper()
    return redirect('index')