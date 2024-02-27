from django.shortcuts import render , get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status =1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    posts = Post.objects.filter(status =1)
    post = get_object_or_404(posts, pk=pid) 
    post.counted_views += 1
    post.save()  
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)
def past_post_list(request):
    past_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'E:/Django course/mysite/templates/blog/past-posts.html', {'past_posts': past_posts})
