from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('',news_view,name='news'),
    path('<int:nid>',news_detail,name='news_detail'),
    path('category/<str:cat_name>',news_view,name='category'),
    path('tag/<str:tag_name>',news_view,name='tag'),
    path('author/<str:author_username>',news_view,name='author'),
    path('search/',news_search,name='search'),
]