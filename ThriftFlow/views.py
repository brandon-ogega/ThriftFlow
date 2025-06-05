from django.shortcuts import render,redirect
from .models import Budget, Expenditure, IncomeSource, Bill, Notification
from .forms import BudgetForm, ExpenditureForm, IncomeSourceForm, BillForm






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

def contact(request):
    return render(request, 'base/contact.html')



def daylo(request):
    return render(request, 'base/daylo.html')


def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('daylo:budget_list')
    else:
        form = BudgetForm()
    return render(request, 'base/budget_list.html', {'budgets': budgets, 'form': form})


def expenditure_list(request):
    expenditures = Expenditure.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user = request.user
            exp.save()
            return redirect('daylo:expenditure_list')
    else:
        form = ExpenditureForm()
    return render(request, 'base/expenditure_list.html', {'expenditures': expenditures, 'form': form})


def income_list(request):
    incomes = IncomeSource.objects.filter(user=request.user)
    if request.method == 'POST':
        form = IncomeSourceForm(request.POST)
        if form.is_valid():
            inc = form.save(commit=False)
            inc.user = request.user
            inc.save()
            return redirect('daylo:income_list')
    else:
        form = IncomeSourceForm()
    return render(request, 'base/income_list.html', {'incomes': incomes, 'form': form})


def bill_list(request):
    bills = Bill.objects.filter(user=request.user)
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.user = request.user
            bill.save()
            return redirect('daylo:bill_list')
    else:
        form = BillForm()
    return render(request, 'base/bill_list.html', {'bills': bills, 'form': form})


def notification_list(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'base/notification_list.html', {'notifications': notifications})



# Create your views here.
