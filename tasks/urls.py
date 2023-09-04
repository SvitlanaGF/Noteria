from django.urls import path, include
from .views import ListOfNotes, Notice, CreateNotice


urlpatterns = [
    path('notes/', ListOfNotes.as_view(), name="notes"),
    path('notice/<int:pk>/', Notice.as_view(), name="notice"),
    path('create-notice/', CreateNotice.as_view(), name="create-notice")
]

