from django.urls import path
from .views import *

app_name = 'mywebsite'

urlpatterns = [
    path('',index_view,name='index'),
    path('donate/',donate_view,name='donate'),
    path('contact/',contact_view,name='contact'),
    path('about/',about_view,name='about'),
    
]
