from django.urls import path
from blog.views import *
from . import views
app_name = 'blog'
urlpatterns = [
    path('', blog_view , name='index'),
    path('<int:pid>', blog_single , name='single'),
    path('category/<str:cat_name>', blog_view , name='category'),
    path('test', test , name='test'),



]