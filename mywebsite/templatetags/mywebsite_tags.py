from django import template
from news.models import News, Category
register = template.Library()

@register.inclusion_tag('mywebsite/last_news.html')
def last_news():
    news = News.objects.filter(status=1).order_by('-published_date')
    news = news.prefetch_related('category')[:3]
    return {'news': news}