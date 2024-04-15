from django.urls import path
from home import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('home')),
    path('home/', views.home_email, name='home'),
]
