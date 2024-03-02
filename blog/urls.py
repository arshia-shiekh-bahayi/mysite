from django.urls import path
from blog.views import *
from . import views
app_name = 'blog'
urlpatterns = [
    path('', blog_view , name='index'),
    path('<int:pid>', blog_single , name='single'),
    path('<int:pid>-1', prev_post , name='prev_post'),
    path('<int:pid>+1', next_post , name='next_post'),
    path('test', test , name='test'),



]