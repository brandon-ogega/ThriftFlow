from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import login_user, logout_user

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('daylo/', views.daylo, name='daylo'),
    path('investments/', views.investments, name='investments'),
    path('profits/', views.profits, name='profits'),
    path('savings/', views.savings, name='savings'),
    path('blog/', views.blog, name='blog'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', logout_user, name='logout'),
    path('accounts/login/', login_user, name='login_user'),
]