from django.contrib.auth import user_logged_in
from django.db import models
import uuid
from django.conf import settings

from django.db.models import ForeignKey


#Create your models here.
class Person(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

class Budget(models.Model):
    TIMEFRAME_CHOICES = [
        ('daily','Daily'),
        ('weekly','Weekly'),
        ('monthly','Monthly'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type =models.CharField(max_length=10, choices=TIMEFRAME_CHOICES)
    item= models.CharField(max_length=50)
    is_recurring = models.BooleanField(default=False)
    expense = models.DecimalField(decimal_places=2, max_digits=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item

class Expenditure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50)
    amount_spent = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField(blank=True)
    date_spent = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type}| {self.amount_spent} spent on {self.date_spent} "


class Saving(models.Model):
    TIMEFRAME_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    saving_goal = models.DecimalField(decimal_places=2, max_digits=12,default=0.00)
    current_amount = models.DecimalField(decimal_places=2, max_digits=12)
    timeframe = models.CharField(max_length=10, choices=TIMEFRAME_CHOICES,default='daily')
    created_at = models.DateTimeField(default=user_logged_in)

    def __str__(self):
        return self.timeframe


class IncomeSource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    date_received = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}-{self.amount} ({self.date_received})"


class Investment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    amount_invested = models.DecimalField(decimal_places=2, max_digits=12)
    expected_return = models.DecimalField(decimal_places=2, max_digits=12, null=True,blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Notification(models.Model):
    TYPE_CHOICES = [
        ('payment_due','Payment due'),
        ('investment','Investment Update'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    message = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type}| {self.message}"



class Bill(models.Model):
    STATUS_CHOICES = [
        ('unpaid','Unpaid'),
        ('paid','Paid'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='unpaid')
    recurring = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type}| {self.amount} spent on {self.due_date} "


class Profit(models.Model):
    source = models.ForeignKey(Investment, on_delete=models.CASCADE,default=Investment)
    income_growth = models.DecimalField(decimal_places=2, max_digits=12,default=0.00)
    amount_invested = models.DecimalField(decimal_places=2, max_digits=12)
    investment_gains = models.DecimalField(decimal_places=2, max_digits=12,default=0.00)
    losses= models.DecimalField(decimal_places=2, max_digits=12,default=0.00)
    total_profit = models.DecimalField(decimal_places=2, max_digits=12,default=0.00)
    created_at = models.DateTimeField(default=user_logged_in)
    updated_at = models.DateTimeField(auto_now=True,)


