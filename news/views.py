from django.shortcuts import render, get_object_or_404
from news.models import News
# Create your views here.
def news_view(request):
    news = News.objects.filter(status=1)
    context = {'news': news}
    return render(request,'news/news.html',context)

def news_detail(request,nid=None):
    news = get_object_or_404(News,pk=nid)
    newss = News.objects.filter(status=1)
    
    i = 0
    while newss[i].id != nid:
        i += 1
    print(newss[i],i)
    if i == 0:
        prev_news = News.objects.get(pk=newss[len(newss) - 1].id)
        next_news = News.objects.get(pk=newss[i+1].id)
    elif i == len(newss) - 1:
        prev_news = News.objects.get(pk=newss[i-1].id)
        next_news = News.objects.get(pk=newss[0].id)
    else:
        prev_news = News.objects.get(pk=newss[i-1].id)
        next_news = News.objects.get(pk=newss[i+1].id)
    # counted_view
    if news:
        news.views = news.views + 1
        news.save()
    context = {'news': news, 'prev_news': prev_news, 'next_news': next_news}
    return render(request,'news/news-detail.html',context)