from django.shortcuts import render
from .models import News

def home(request):
    news = { 'news': News.objects.all()}
    return render(request, 'news/index.html', news)

# Create your views here.
