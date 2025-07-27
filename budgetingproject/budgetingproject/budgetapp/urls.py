from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
]
