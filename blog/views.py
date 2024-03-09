from django.shortcuts import render , get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1 ,published_date__lte=timezone.now()).order_by('-published_date')
    if kwargs.get('cat_name') != None:
     posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
     posts = posts.filter(author__username=kwargs['author_username'])
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = Post.objects.filter(status =1,published_date__lte=timezone.now()).order_by('-published_date')
    post = get_object_or_404(posts, pk=pid) 
    post.counted_views += 1
    post.save() 
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

def blog_search(request):
   posts = Post.objects.filter(status=1)
   if request.method == 'GET':
      if s := request.GET.get('s'):
       posts = posts.filter(content__contains=s)
   context = {'posts':posts}
   return render(request,'blog/blog-home.html',context)