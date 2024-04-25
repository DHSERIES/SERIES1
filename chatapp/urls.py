from django.urls import path, include
from . import views as chat_views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    # Chat Page
    path("", chat_views.chatPage, name="chat-page"),
    
    # Authentication URLs
    path("auth/login/", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
    path('auth/logout/', LogoutView.as_view(next_page='login-user'), name='logout-user'),

]

