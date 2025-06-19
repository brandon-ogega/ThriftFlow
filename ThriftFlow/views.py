from django.shortcuts import render,redirect
from .models import (Investment, Saving,Budget, Bill, Notification,Profit)
from .forms import (InvestmentForm, SavingForm, BudgetForm,
                    ExpenditureForm,BillForm, NotificationForm, ProfitForm)

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'Username not found')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.error(request, f"Welcome home{username}!")
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request,"base/login.html")

def createUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Error creating account')
    else:
        form = UserCreationForm()

    return render(request, 'base/register.html', {'form': form})

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
@login_required(login_url="login")
def investments(request):
    investments = Investment.objects.all()
    context = {"investments": investments}
    return render(request, 'base/investments.html',context)


@login_required(login_url="login")
def investment(request,pk):
    investment = Investment.objects.get(id=pk)
    context = {"investment":investment}
    return render(request, 'base/investment.html',context)


@login_required(login_url="login")
def updateInvestment(request, pk):
    investment = Investment.objects.get(id=pk)
    form = InvestmentForm(instance=investment)
    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance=investment)
        form.save()
        return redirect('investments')

    context = {'form': form,"from":"update"}
    return render(request,'base/investment_form.html', context)

@login_required(login_url="login")
def deleteInvestment(request, pk):
    investment = Investment.objects.get(id=pk)
    context ={"investment":investment}
    if request.method == "POST":
        investment.delete()
        return redirect('investments')
    return render(request, 'base/delete_form.html', context)

def home(request):
    bills = Bill.objects.all()
    """
     - get all bills check the most recent and soon to expire,
     - use the due date ( get the due dat difference from the current date) 
    
    """
    return render(request, 'base/home.html')
def about(request):
    return render(request, 'base/about.html')


@login_required(login_url="login")
def profit(request,pk):
    profit = Profit.objects.get(id=pk)
    context = {"profit":profit}
    return render(request, 'base/profit.html',context)


@login_required(login_url="login")
def profits(request):
    profits = Profit.objects.all()
    context = {"profits": profits}
    return render(request, 'base/profits.html',context)


@login_required(login_url="login")
def showProfits(request):
    form = ProfitForm()
    if request.method == "POST":
        form = ProfitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profits")
    context = {"form": form,"from":"create"}
    return render(request,'base/profit_form.html',context)

@login_required(login_url="login")
def saving(request,pk):
    saving = Saving.objects.get(id=pk)
    context = {"saving":saving}
    return render(request, 'base/saving.html',context)


@login_required(login_url="login")
def savings(request):
    savings = Saving.objects.all()
    context = {'savings':savings}
    return render(request, 'base/savings.html',context)


@login_required(login_url="login")
def createSavings(request):
    form = SavingForm()
    if request.method == "POST":
        form = SavingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("savings")

    context = {"form": form,"from":"create"}
    return render(request,'base/savings_form.html',context)

def updateSavings(request, pk):
    saving = Saving.objects.get(id=pk)
    form = SavingForm(instance=saving)
    if request.method == "POST":
        form = SavingForm(request.POST, instance=saving)
        form.save()
        return redirect("savings")
    context = {'form': form,"from":"update"}
    return render(request,'base/savings_form.html',context)

@login_required(login_url="login")
def deleteSaving(request, pk):
    saving = Saving.objects.get(id=pk)
    context ={"saving":saving}
    if request.method == "POST":
        saving.delete()
        return redirect('savings')
    return render(request, 'base/delete_form.html', context)




def contact(request):
    return render(request, 'base/contact.html')


@login_required(login_url="login")
def daylo(request):
    bills = Bill.objects.all()
    notifications = Notification.objects.all()
    budgets = Budget.objects.all()
    context = {'bills':bills,'notifications':notifications,'budgets':budgets}
    return render(request, 'base/daylo.html',context)

def budget(request,pk):
    budget = Budget.objects.get(id=pk)
    context = {'budget':budget}
    return render(request, 'base/budget.html',context)



def updateBudget(request,pk):
    budget = Budget.objects.get(id=pk)
    form = BudgetForm(instance=budget)
    if request.method == "POST":
        form = BudgetForm(request.POST, instance=budget)
        form.save()
        return redirect("daylo")
    context = {'form': form,"from":"update"}
    return render(request, 'base/budget_form.html',context)

@login_required(login_url="login")
def createBudget(request):
    form = BudgetForm()
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("daylo")
    context = {"form": form,"from":"create"}
    return render(request,'base/budget_form.html',context)

@login_required(login_url="login")
def deleteBudget(request, pk):
    budget = Budget.objects.get(id=pk)
    context ={"budget":budget}
    if request.method == "POST":
        budget.delete()
        return redirect('daylo')
    return render(request, 'base/delete_form.html', context)


@login_required(login_url="login")
def createExpenditure(request):
    form = ExpenditureForm()
    if request.method == "POST":
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("daylo")
    context = {"form": form,"from":"create"}
    return render(request,'base/daylo.html',context)

@login_required(login_url="login")
def createNotification(request):
    form = NotificationForm()
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("daylo")
    context = {"form": form,"from":"create"}
    return render(request,'base/notification_form.html',context)

@login_required(login_url="login")
def createBill(request):
    form = BillForm()
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("daylo")
    context = {"form": form,"from":"create"}
    return render(request,'base/bill_form.html',context)

def bill(request,pk):
    bill = Bill.objects.get(id=pk)
    context = {'bill':bill}
    return render(request, 'base/bill.html',context)

def updateBill(request,pk):
    bill = Bill.objects.get(id=pk)
    form = BillForm(instance=bill)
    if request.method == "POST":
        form = BillForm(request.POST, instance=bill)
        form.save()
        return redirect("daylo")
    context = {'form': form,"from":"update"}
    return render(request, 'base/bill_form.html',context)

@login_required(login_url="login")
def deleteBill(request, pk):
    bill = Bill.objects.get(id=pk)
    context ={"bill":bill}
    if request.method == "POST":
        bill.delete()
        return redirect('daylo')
    return render(request, 'base/delete_form.html', context)


def notifications(request):
    notifications = Notification.objects.all()
    context = {'notifications':notifications}
    return render(request, 'base/notifications.html', context)


#Create your views here.
