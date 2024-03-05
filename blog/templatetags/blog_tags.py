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
@register.filter
def snippet(value,arg=20):
    return value[:arg]+'...'
@register.inclusion_tag("popularposts.html")
def popularposts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:3]
    return {"posts": posts}


