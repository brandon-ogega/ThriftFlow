from django import forms
from .models import (Budget, Expenditure, Bill, Investment, Saving, Notification, Profit)


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'

class ExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields ='__all__'


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['name', 'amount_invested', 'expected_return', 'actual_return', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class SavingForm(forms.ModelForm):
    class Meta:
        model = Saving
        fields = '__all__'

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'


class ProfitForm(forms.ModelForm):
    class Meta:
        model = Profit
        fields = '__all__'