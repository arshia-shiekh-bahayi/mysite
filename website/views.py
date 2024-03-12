from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from blog.models import Post
from django.core.paginator import Paginator
from website.models import Contact
from website.forms import NameForm, ContactForm , NewsletterForm
def index_view(request,arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    posts = Paginator(posts,2)
    context = {'posts': posts}
    return render(request,'website/index.html',context)

def about_view(request):
        return render(request,'website/about.html')

def contact_view(request):
        if request.method == 'POST':
               form = ContactForm(request.POST)
               if form.is_valid():
                      form.save()
        form = ContactForm()              
        return render(request,'website/contact.html',{"form":form})

def newsletter_view(request):
       if request.method == 'POST':
              form = NewsletterForm(request.POST)
              if form.is_valid():
                     form.save()
                     HttpResponseRedirect('/')                    
              else :
                     HttpResponseRedirect('/')                     
       form  =ContactForm()
       return render(request,'newsletter.html',{'form':form})

def test_view(request):
       if request.method == 'POST':
              form = ContactForm(request.POST)
              if form.is_valid():
                     form.save()
                     return HttpResponse('done')                     
              else :
                     return HttpResponse("not valid")                     
       form  =ContactForm()
       return render(request,'test.html',{'form':form})

