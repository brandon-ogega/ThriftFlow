from django.shortcuts import render, redirect
from .models import Bill, Notification, IncomeSource, Budget
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def investments(request):
    return render(request, 'base/investments.html')

def profits(request):
    return render(request, 'base/profits.html')

def savings(request):
    return render(request, 'base/savings.html')

def blog(request):
    return render(request, 'base/blog.html')

@login_required
def daylo(request):
    bills = Bill.objects.filter(user=request.user)
    notifications = Notification.objects.filter(user=request.user)
    income_sources = IncomeSource.objects.filter(user=request.user)
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'base/daylo.html', {
        'bills': bills,
        'notifications': notifications,
        'income_sources': income_sources,
        'budgets': budgets,
    })
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'base/login.html')
    
def logout_user(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, "See u soon")
    return render(request, "base/logout.html")
# Create your views here.
