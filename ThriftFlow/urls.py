from django.urls import path
from . import views




urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('daylo/', views.daylo, name='daylo'),
    path('investments/', views.investments, name='investments'),
    path('profits/', views.profits, name='profits'),
    path('savings/', views.savings, name='savings'),
    path('blog/', views.blog, name='blog'),
    path('budgets/', views.budget_list, name='budget_list'),
    path('expenditures/', views.expenditure_list, name='expenditure_list'),
    path('incomes/', views.income_list, name='income_list'),
    path('bills/', views.bill_list, name='bill_list'),
    path('notifications/', views.notification_list, name='notification_list'),
]