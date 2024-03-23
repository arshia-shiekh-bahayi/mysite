from django.shortcuts import render , get_object_or_404 , HttpResponse
from blog.models import Post , Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1 ,published_date__lte=timezone.now()).order_by('-published_date')
    
    if kwargs.get('cat_name') != None:
     posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
     posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
     posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts,3)
    try:
     page_number = request.GET.get('page')
     posts = posts.get_page(page_number)
    except PageNotAnInteger:
     posts = posts.get_page(2)
    except EmptyPage:
     posts = posts.get_page(1)
       
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    if request.method == 'POST':
     form = CommentForm(request.POST)
     if form.is_valid():
       form.save()
       messages.add_message(request,messages.SUCCESS,'your ticket had been submited successfully')
     else :
       messages.add_message(request,messages.ERROR,'Your ticket was not submitted')
      
    posts = Post.objects.filter(status =1,published_date__lte=timezone.now()).order_by('-published_date')
    post = get_object_or_404(posts, pk=pid) 
    comments = Comment.objects.filter(post=post.id,approved=True).order_by('-created_date')
    number_of_comments = comments.count
    post.counted_views += 1
    post.save() 
    now = timezone.now()
    next_post = Post.objects.filter(status=1, published_date__gt=post.published_date, published_date__lt=now).order_by('published_date').first()
    prev_post = Post.objects.filter(status=1, published_date__lt=post.published_date).order_by('published_date').last()
    form = CommentForm()
    context = {'post':post,'next_post':next_post,'prev_post':prev_post,'comments':comments,'number_of_comments':number_of_comments,'form':form}
    return render(request,'blog/blog-single.html',context)

def blog_search(request):
   posts = Post.objects.filter(status=1)
   if request.method == 'GET':
      if s := request.GET.get('s'):
       posts = posts.filter(content__contains=s)
   context = {'posts':posts}
   return render(request,'blog/blog-home.html',context)

def test(request):
    return render(request,'test.html')
