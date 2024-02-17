from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('',news_view,name='news'),
    path('<int:nid>',news_detail,name='news_detail'),
    
]