from django.shortcuts import render, get_object_or_404
from news.models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
# Create your views here.
def news_view(request,**kwargs):
    news = News.objects.filter(status=1)

    if kwargs.get('cat_name') != None:
        news = news.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        news = news.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        news = news.filter(tags__name__in=[kwargs['tag_name']])
    
    news = Paginator(news,3)
    try:
        page_number = request.GET.get('page')
        news = news.get_page(page_number)
    except PageNotAnInteger:
        news = news.get_page(1)
    except EmptyPage:
        news = news.get_page(1)
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

def news_search(request):
    news = News.objects.filter(status = 1)
    if request.method == 'GET':
        if s := request.GET.get('s'): 
            news = news.filter(content__contains=request.GET.get('s'))
    context = {'news': news}
    return render(request,'news/news.html',context)