from django.urls import path
from blog.views import *
from . import views

app_name = 'blog'
urlpatterns = [
    path('', blog_view , name='index'),
    path('<int:pid>', blog_single , name='single'),
    #path('post-<int:pid>', test , name='test'),
    path('past-posts/', past_post_list, name='past-posts.html'),


]