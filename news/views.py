from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from news.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def news_view(request,**kwargs):
    news = News.objects.filter(status=1).order_by('published_date')

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
    newss = News.objects.filter(status=1).order_by('published_date')
    
    comments = Comments.objects.filter(news=news.id,approved=True).order_by('created_date')
    form = CommentForm()

    if news.login_require == True and not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts:login'))



    # Handle form submission
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submited successfully')
    
    
    i = 0
    while newss[i].id != nid:
        i += 1
   
    if i == 0:
        next_news = News.objects.get(pk=newss[i+1].id)
    elif i == len(newss) - 1:
        prev_news = News.objects.get(pk=newss[i-1].id)
    else:
        prev_news = News.objects.get(pk=newss[i-1].id)
        next_news = News.objects.get(pk=newss[i+1].id)

    # counted_view
    if news:
        news.views = news.views + 1
        news.save()
    print(news.id)
    context = {'news': news,
               'comments': comments,
               'form': form,
            }
    if i == 0:
        context['next_news'] = next_news
    elif i == len(newss) - 1: 
        context['prev_news'] = prev_news
    else:
        context['next_news'] = next_news
        context['prev_news'] = prev_news

    return render(request,'news/news-detail.html',context)

def news_search(request):
    news = News.objects.filter(status = 1)
    if request.method == 'GET':
        if s := request.GET.get('s'): 
            news = news.filter(content__contains=request.GET.get('s'))
    context = {'news': news}
    return render(request,'news/news.html',context)