from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('daylo/', views.daylo, name='daylo'),
    path('investments/', views.investments, name='investments'),
    path('profits/', views.profits, name='profits'),
    path('savings/', views.savings, name='savings'),
    path('blog/', views.blog, name='blog'),
]