from django.urls import path
from . import views
app_name = 'slinks'  # namespace for slinks app
# defining url patterns for slinks app
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create, name='create'),
    path('<str:short_key>/', views.redirect_view, name='redirect_view'),
    path('edit/<str:short_key>/', views.edit, name='edit'),
    path('delete/<str:short_key>/', views.delete, name='delete'),
]