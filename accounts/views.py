from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        msg = f'You are already logged in as {request.user.username}'
    else:
        msg = 'You are not logged in'
    return render(request, 'accounts/login.html', {'msg': msg})
#def logout_view(request):
#   return render(request, 'logout.html')
def singup_view(request):
    return render(request,'accounts/singup.html')