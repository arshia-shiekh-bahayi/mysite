from django.urls import path
from accounts.views import (
    login_view,
    login_email_view,
    logout_view,
    signup_view,
    forgot_password_view,
)

app_name = "accounts"
urlpatterns = [
    path("login", login_view, name="login"),
    path("login_email", login_email_view, name="login_email"),
    path("logout", logout_view, name="logout"),
    path("signup", signup_view, name="signup"),
    path("forgot_password", forgot_password_view, name="forgot_password"),
]
