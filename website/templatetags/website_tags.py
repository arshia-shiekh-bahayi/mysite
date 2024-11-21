from django import template
from blog.models import Post, Category
from django.utils import timezone

register = template.Library()


@register.inclusion_tag("website/latestposts.html")
def latestposts(arg=6):
    now = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lt=now).order_by(
        "-published_date"
    )[:arg]
    return {"posts": posts}
