from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.urls import reverse
from accounts.models import UserData
from django.contrib.auth.models import User
from accounts.forms import  Email_AuthenticationForm, SignUpForm

# Create your views here.
##
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')

        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')
##
def login_email_view(request):
    if not request.user.is_authenticated:
        print('1')
        if request.method == 'POST':
            print('2')
            form = Email_AuthenticationForm(request.POST)
            if form.is_valid():
             print('3')
             email = form.cleaned_data.get('username')
             try:
              username = User.objects.get(email=email).username
             except:
                 return HttpResponse('wrong')
             password = form.cleaned_data.get('password')
             user = authenticate(request, username=username, password=password)
             if user is not None:
                 print("4")
                 login(request,user)
                 return redirect('/')

        form = Email_AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login-email.html',context)
    else:
        return redirect('/')

##     
def logout_view(request):
    if not request.user.is_authenticated:
       return render(request, 'accounts/login.html')
    elif request.user.is_authenticated :
     logout(request)
     return redirect('/')
##

   
#def signup_view(request):
#    if not request.user.is_authenticated:
#        if request.method == 'POST':
#            form = UserCreationForm(request.POST)
#            if form.is_valid():
#                form.save()
#                return HttpResponseRedirect(reverse('accounts:login'))
#        form = UserCreationForm()
#        context = {'form':form}
#        return render(request,'accounts/signup.html',context)
#    else:
#        return redirect('/')
    
##    
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = User.objects.get(username=username)
            user_data = UserData.objects.create(user=user,email=email)
            user_data.save()
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})
##

