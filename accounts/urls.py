from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login', views.login_view, name='login'),
    path('login_email', views.login_email_view, name='login_email'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup_view, name='signup'),
]