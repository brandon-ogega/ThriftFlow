from django.urls import path
from . import views
from . views import loginUser,logoutUser




urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.createUser, name='register'),
    path('about/', views.about, name='about'),
    path('daylo/', views.daylo, name='daylo'),
    path('investments/', views.investments, name='investments'),
    path('profits/', views.profits, name='profits'),
    path('profit/<str:pk>/', views.profit, name='profit'),
    path('savings/', views.savings, name='savings'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('create_investment/', views.createInvestment, name='create_investment'),
    path('update_investment/<str:pk>/', views.updateInvestment, name='update_investment'),
    path('investment/<str:pk>/', views.investment, name='investment'),
    path('create_savings/', views.createSavings, name='create_savings'),
    path('create_budget/', views.createBudget, name='create_budget'),
    path('budget/<str:pk>/', views.budget, name='budget'),
    path('update_budget/<str:pk>/', views.updateBudget, name='update_budget'),
    path('create_notification/', views.createNotification, name='create_notification'),
    path('create_expenditure/', views.createExpenditure, name='create_expenditure'),
    path('show_profits/', views.showProfits, name='show_profits'),
    path('create_bill/', views.createBill, name='create_bill'),

]