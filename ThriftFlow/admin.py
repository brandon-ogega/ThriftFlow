from django.contrib import admin
from .models import Budget, Expenditure, IncomeSource, Notification, Bill

admin.site.register(Budget)
admin.site.register(Expenditure)
admin.site.register(IncomeSource)
admin.site.register(Notification)
admin.site.register(Bill)



# Register your models here.
