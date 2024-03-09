from django.shortcuts import render , get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_view(request, cat_name=None):
    posts = Post.objects.filter(status=1 ,published_date__lte=timezone.now()).order_by('-published_date')
    if cat_name:
     posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    posts = Post.objects.filter(status =1,published_date__lte=timezone.now()).order_by('-published_date')
    post = get_object_or_404(posts, pk=pid) 
    post.counted_views += 1
    post.save() 
    post_published_date= post.published_date
    next_post = Post.objects.filter(status=1, published_date__gt=post.published_date).order_by('published_date').first()
    prev_post = Post.objects.filter(status=1, published_date__lt=post.published_date).order_by('published_date').last()

    context = {'post':post,'next_post':next_post,'prev_post':prev_post}
    return render(request,'blog/blog-single.html',context)
def test(request):
    return render(request,'test.html')
def blog_category(request, cat_name):
   posts = Post.objects.filter(status=1)
   posts = posts.filter(category__name=cat_name)
   context = {'posts':posts}
   return render(request,'blog/blog-home.html',context)