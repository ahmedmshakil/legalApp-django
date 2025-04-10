# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('experts/', views.expert_list, name='expert_list'),
    path('experts/<int:pk>/', views.expert_detail, name='expert_detail'),
    # Add other URL patterns as needed
]