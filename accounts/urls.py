from django.urls import path
from . import views
from django.urls import path
from accounts.views import *
app_name = 'accounts'
urlpatterns = [
    path('login', login_view, name='login'),
    path('login_email', login_email_view, name='login_email'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
]