from django.shortcuts import render,redirect
from .models import (Investment, Saving,Budget, Bill, Notification, Expenditure, Profit)
from .forms import (InvestmentForm, SavingForm, BudgetForm,
                    ExpenditureForm,BillForm, NotificationForm, ProfitForm)

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def loginUser(request,user):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username not found')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.error(request, f"Welcome home{username}!")
        else:
            messages.error(request, 'Invalid username or password')

    return render(request,"base/login.html")

def logoutUser(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, "You have been logged out")
        return redirect("login")
    return render(request,"base/logout_form.html")

def createInvestment(request):
    form = InvestmentForm()
    if request.method == "POST":
        form = InvestmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("investments")

    context = {"form": form,"from":"create"}
    return render(request,'base/investment_form.html',context)

def investments(request):
    investments = Investment.objects.all()
    context = {"investments": investments}
    return render(request, 'base/investments.html',context)

def investment(request,pk):
    investment = Investment.objects.all(id=pk)
    context = {"investment":investment}
    return render(request, 'base/investment.html',context)
def home(request):
    return render(request, 'base/home.html')
def about(request):
    return render(request, 'base/about.html')

def profit(request,pk):
    profit = Profit.objects.all(id=pk)
    context = {"profit":profit}
    return render(request, 'base/profit.html',context)

def profits(request):
    profits = Profit.objects.all()
    context = {"profits": profits}
    return render(request, 'base/profits.html',context)
def showProfits(request):
    form = ProfitForm()
    if request.method == "POST":
        form = ProfitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profits")
    context = {"form": form,"from":"create"}
    return render(request,'base/profit_form.html',context)

def savings(request):
    savings = Saving.objects.all()
    context = {'savings':savings}
    return render(request, 'base/savings.html',context)

def createSavings(request):
    form = SavingForm()
    if request.method == "POST":
        form = SavingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("savings")

    context = {"form": form,"from":"create"}
    return render(request,'base/savings_form.html',context)

def blog(request):
    return render(request, 'base/blog.html')

def contact(request):
    return render(request, 'base/contact.html')



def daylo(request):
    bills = Bill.objects.all()
    notifications = Notification.objects.all()
    budgets = Budget.objects.all()
    context = {'bills':bills,'notifications':notifications,'budgets':budgets}
    return render(request, 'base/daylo.html',context)

def createBudget(request):
    form = BudgetForm()
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("daylo")
    context = {"form": form,"from":"create"}
    return render(request,'base/daylo.html',context)

def createExpenditure(request):
    form = ExpenditureForm()
    if request.method == "POST":
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("daylo")
    context = {"form": form,"from":"create"}
    return render(request,'base/daylo.html',context)

def createNotification(request):
    form = NotificationForm()
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("daylo")
    context = {"form": form,"from":"create"}
    return render(request,'base/daylo.html',context)





# Create your views here.
