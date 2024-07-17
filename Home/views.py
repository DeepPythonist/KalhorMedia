from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Articles.models import Article, Category
from Accounts.models import Account
from Ads.models import Ads


# Create your views here.


def home(request):

    ads = Ads.objects.last()
    all_articles = Article.objects.all().order_by('created_at')
    articles_by_view = all_articles.all().order_by('-views')[:4]
    page = request.GET.get('page')
    paginator = Paginator(all_articles, 4)
    try:
        page_list = paginator.get_page(page)
    except PageNotAnInteger:
        page_list = paginator.get_page(1)
    except EmptyPage:
        page_list = paginator.get_page(paginator.num_pages)

    context = {
        'ads': ads,
        'page_list': page_list,
        'all_articles': all_articles,
    }
    return render(request, 'home.html', context=context)


def author(request, name):
    articles = get_object_or_404(Account, full_name=name)
    articles_author = articles.article_set.all().order_by('created_at')
    page = request.GET.get('page')
    paginator = Paginator(articles_author, 4)
    try:
        page_list = paginator.get_page(page)
    except PageNotAnInteger:
        page_list = paginator.get_page(1)
    except EmptyPage:
        page_list = paginator.get_page(paginator.num_pages)

    context = {
        'page_list': page_list,
        'count_articles': len(articles_author),
        'articles': articles,
    }
    return render(request, 'author.html', context=context)


def category_detail(request, name):
    category_info = get_object_or_404(Category, name=name)
    ads = Ads.objects.last()
    all_articles = category_info.article_set.all().order_by('created_at')
    page = request.GET.get('page')
    paginator = Paginator(all_articles, 4)
    try:
        page_list = paginator.get_page(page)
    except PageNotAnInteger:
        page_list = paginator.get_page(1)
    except EmptyPage:
        page_list = paginator.get_page(paginator.num_pages)

    context = {
        'ads': ads,
        'all_articles': all_articles,
        'page_list': page_list,
    }
    return render(request, 'category_details.html', context=context)


def article_detail(request, name):
    article = get_object_or_404(Article, title=name)
    article.views += 1
    article.save()
    if article.keywords:
        keywords = article.keywords.split('-')
        new_keywords = []
        for keyword in keywords:
            s = keyword.replace(' ', '_')
            new_keywords.append(s)
    else:
        new_keywords = []

    context = {
        'article': article,
        'keywords': new_keywords,
    }
    return render(request, 'article_details.html', context)


def about(request):
    return render(request, 'about_us.html')


def handler404(request, exception):
    return render(request, '404.html', status=404)
