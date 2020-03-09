from django.shortcuts import render
from .models import Article
import random


def index(request):
    all_article = Article.objects.order_by("-article_data")
    last_article = all_article[0]
    all_article = all_article[1:]
    random_article = all_article[random.randrange(len(all_article))]
    return render(request, 'main/index.html', {'last_article': last_article, 'random_article': random_article})
