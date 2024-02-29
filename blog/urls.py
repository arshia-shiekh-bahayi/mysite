from django.urls import path
from blog.views import *
from . import views
app_name = 'blog'
urlpatterns = [
    path('', blog_view , name='index'),
    path('<int:pid>', blog_single , name='single'),
    path('prev/<int:pid>', prev_post , name='prev_post'),
    path('next<int:pid>', next_post , name='next_post'),


]