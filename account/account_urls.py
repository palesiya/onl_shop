from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import LoginView, register, logout_view


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

]
