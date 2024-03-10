from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blog.models import Post
from django.core.paginator import Paginator
from website.models import Contact
def index_view(request,arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    posts = Paginator(posts,2)
    context = {'posts': posts}
    return render(request,'website/index.html',context)
def about_view(request):
        return render(request,'website/about.html')
def contact_view(request):
        return render(request,'website/contact.html')
def test_view(request):
       if request.method == 'POST':
              name = request.POST.get('name')
              email = request.POST.get('email')
              subject = request.POST.get('subject')
              message = request.POST.get('message')
              print(name,email,subject,message)
              c = Contact()
              c.name=name
              c.email=email
              c.subject=subject
              c.message=message
              c.save()
       return render(request,'test.html',{})

