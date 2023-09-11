from django.urls import path, include
from .views import ListOfNotes, Notice, CreateNotice, UpdateNotice, DeleteNotice, Login, main, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('notes/', ListOfNotes.as_view(), name="notes"),
    path('notice/<int:pk>/', Notice.as_view(), name="notice"),
    path('create-notice/', CreateNotice.as_view(), name="create-notice"),
    path('notice-edit/<int:pk>/', UpdateNotice.as_view(), name="notice-edit"),
    path('notice-delete/<int:pk>/', DeleteNotice.as_view(), name="notice-delete"),
    path('', main, name="main"),
    path('login/', Login, name="login"),
    path('logout/', LogoutView.as_view(next_page='main'), name="logout"),
    path('register/', register, name="register")
]

