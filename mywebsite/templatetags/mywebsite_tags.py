from django import template
from news.models import News, Category
register = template.Library()

@register.inclusion_tag('mywebsite/last_news.html')
def last_news():
    news = News.objects.filter(status=True).prefetch_related('category')[:4]
    
    return {'news': news}