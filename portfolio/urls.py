from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name = 'register'),
    path('login/', views.userlogin, name = 'login'),
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
]