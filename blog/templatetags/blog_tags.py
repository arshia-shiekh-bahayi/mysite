from django import template
from blog.models import Post 
from taggit.models import Tag
from blog.models import Category
from django.shortcuts import get_object_or_404
from django.utils import timezone
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
@register.inclusion_tag("blog/popularposts.html")
def latestposts(arg=3):
    now = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lt=now).order_by('-published_date')[:arg]
    return {"posts": posts}


@register.inclusion_tag("blog/post-categories.html")
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categories":cat_dict}
@register.inclusion_tag("blog/homeblog-tags.html")
def tags():
    posts = Post.objects.filter(status=1)
    tags = Tag.objects.all()
    tags_dict = {}
    for tag_name in tags:
        tags_dict[tag_name]= posts.filter(tags=tag_name)
    return{"tags":tags_dict}
