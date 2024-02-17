from django.shortcuts import render, get_object_or_404
from news.models import News
# Create your views here.
def news_view(request):
    news = News.objects.filter(status=1)
    context = {'news': news}
    return render(request,'news/news.html',context)

def news_detail(request,nid=None):
    news = get_object_or_404(News,pk=nid)

    # counted_view
    if news:
        news.views = news.views + 1
        news.save()
    context = {'news': news}
    return render(request,'news/news-detail.html',context)