from django import forms
from .models import Budget, Expenditure, IncomeSource, Bill

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'allocated_amount', 'actual_amount', 'timeframe', 'is_recurring']

class ExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ['category', 'amount_spent', 'description', 'date_spent']

class IncomeSourceForm(forms.ModelForm):
    class Meta:
        model = IncomeSource
        fields = ['title', 'amount', 'date_received', 'is_recurring', 'notes']

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['title', 'amount', 'due_date', 'status', 'recurring', 'notes']
