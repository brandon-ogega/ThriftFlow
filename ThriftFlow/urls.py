from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('daylo/', views.daylo, name='daylo'),
    path('investments/', views.investments, name='investments'),
    path('profits/', views.profits, name='profits'),
    path('profit/<str:pk>/', views.profit, name='profit'),
    path('savings/', views.savings, name='savings'),
    path('blog/', views.blog, name='blog'),
    path('login/', views .login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create_investment/', views.createInvestment, name='create_investment'),
    path('update_investment/<str:pk>/', views.updateInvestment, name='update_investment'),
    path('investment/<str:pk>/', views.investment, name='investment'),
    path('create_savings/', views.createSavings, name='create_savings'),
    path('create_budget/', views.createBudget, name='create_budget'),
    path('create_notification/', views.createNotification, name='create_notification'),
    path('create_expenditure/', views.createExpenditure, name='create_expenditure'),
    path('show_profits/', views.showProfits, name='show_profits'),

]