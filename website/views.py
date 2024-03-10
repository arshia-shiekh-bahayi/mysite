from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blog.models import Post
from django.core.paginator import Paginator
def index_view(request,arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    posts = Paginator(posts,2)
    context = {'posts': posts}
    return render(request,'website/index.html',context)

def about_view(request):
        return render(request,'website/about.html')
def contact_view(request):
        return render(request,'website/contact.html')

