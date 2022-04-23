from django.shortcuts import render
from django.http.response import HttpResponse

from news.models import News

def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss': newss})