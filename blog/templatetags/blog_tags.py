from django import template
from blog.models import Post
from django.shortcuts import get_object_or_404
register = template.Library()
@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts
@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts
@register.simple_tag(name='prev_post')
def function(pid):
    posts = Post.objects.filter(status=1)
    post  = get_object_or_404(posts , pk= pid-1)
    return post
@register.simple_tag(name='next_post')
def function(pid):
    posts = Post.objects.filter(status=1)
    post  = get_object_or_404(posts , pk= pid+1)
    return post