from django.contrib import admin
from .models import Balance
# Register your models here.


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')