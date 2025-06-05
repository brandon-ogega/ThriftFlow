from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid



#Create your models here.

class Budget(models.Model):
    TIMEFRAME_CHOICES = [
        ('daily','Daily'),
        ('weekly','Weekly'),
        ('monthly','Monthly'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=50)
    is_recurring = models.BooleanField(default=False)
    allocated_amount = models.DecimalField(decimal_places=2, max_digits=12)
    actual_amount = models.DecimalField(decimal_places=2, max_digits=12)
    timeframe = models.CharField(max_length=10,choices=TIMEFRAME_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

class Expenditure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=50)
    amount_spent = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField(blank=True)
    date_spent = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category}| {self.amount_spent} spent on {self.date_spent} "

class SavingGoal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    related_name = 'saving_goals'
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    target_amount = models.DecimalField(decimal_places=2, max_digits=12)
    current_amount = models.DecimalField(decimal_places=2, max_digits=12,default=0)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}| Target: {self.target_amount} | Saved:{self.current_amount}"

class Saving(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goal = models.ForeignKey(SavingGoal,null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    date_saved = models.DateField()
    note =models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.goal}| {self.amount} spent on {self.date_saved} "


class IncomeSource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    date_received = models.DateField()
    is_recurring = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}-{self.amount} ({self.date_received})"

class IncomeAllocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    income_source = models.ForeignKey(IncomeSource, on_delete=models.CASCADE)
    related_name = 'allocations'
    amount_allocated = models.DecimalField(decimal_places=2, max_digits=12)
    allocated_on = models.DateField(auto_now_add=True)
    purpose = models.CharField(max_length=100, default='Investment')

    def __str__(self):
        return f"Allocated{self.amount_allocated} from{self.income_source.title} on {self.allocated_on}"


class Investment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    income_allocation = models.ForeignKey(IncomeAllocation, on_delete=models.SET_NULL, null=True,blank=True)
    name = models.CharField(max_length=100)
    amount_invested = models.DecimalField(decimal_places=2, max_digits=12)
    expected_return = models.DecimalField(decimal_places=2, max_digits=12)
    actual_return = models.DecimalField(decimal_places=2, max_digits=12, null=True,blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def profit(self):
        if self.actual_return:
            return self.actual_return - self.amount_invested
        return None
    def __str__(self):
        return f"{self.name}| Invested: {self.amount_invested}| Expected Return: {self.expected_return}"


class Notification(models.Model):
    TYPE_CHOICES = [
        ('payment_due','Payment due'),
        ('goal_progress','Goal progress'),
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
    title = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='unpaid')
    recurring = models.BooleanField(default=False)
    notes = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}-{self.amount}('Recurring' {self.recurring if self.recurring else 'one-time'})"

class Report(models.Model):
    TYPE_CHOICES = [
        ('weekly','Weekly'),
        ('monthly','Monthly'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    from_date = models.DateField()
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type}| {self.data}"


