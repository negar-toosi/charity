from django import template
from news.models import News,Category, Comments
register = template.Library()

@register.inclusion_tag('news/recent-news.html')
def recent_news():
    news = News.objects.filter(status=1).order_by('-published_date')[:2]
    return {'news': news}

@register.inclusion_tag('news/news-Categories.html')
def newsCategories():
    news = News.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = news.filter(category=name).count()
    return {'categories': cat_dict}

@register.simple_tag(name='comments_count')
def function(nid):
    return Comments.objects.filter(news=nid).count()