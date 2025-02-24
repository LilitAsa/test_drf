from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostApiView.as_view()),
    path('posts/<int:pk>/', views.PostApiView.as_view()),
]
