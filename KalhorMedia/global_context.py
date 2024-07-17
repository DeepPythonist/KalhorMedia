from Articles.models import Article, Category


def get_categories(request):
    categories = Category.objects.all().order_by('-created_at')
    return {'all_categories': categories}


def get_top_articles(request):
    articles = Article.objects.all().order_by('created_at')
    articles_by_view = articles.order_by('-views')[:4]
    return {'articles_by_view': articles_by_view}
