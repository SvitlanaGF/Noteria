from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('login/', views.Login, name="login"),
    path('register/', views.register, name="register"),
    path()
]

