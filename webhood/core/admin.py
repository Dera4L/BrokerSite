from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')
    
   

    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'coin','payment_description','amount','transaction_id','confirmed')