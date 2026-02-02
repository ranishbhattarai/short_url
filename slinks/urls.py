from django.urls import path
from . import views
app_name = 'slinks'  # namespace for slinks app
# defining url patterns for slinks app
urlpatterns = [
    path('', views.home, name='home'),# home page
    path('dashboard/', views.dashboard, name='dashboard'),# user dashboard
    path('create/', views.create, name='create'),# create new short link
    path('<str:short_key>/', views.redirect_view, name='redirect_view'),# redirect short link
    path('edit/<str:short_key>/', views.edit, name='edit'),# edit short link
    path('delete/<str:short_key>/', views.delete, name='delete'),# delete short link
]