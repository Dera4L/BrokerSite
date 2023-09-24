from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')
    
   

    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'coin','payment_description','amount','transaction_id','confirmed')
    
    
@admin.register(BitcoinAddress)
class BitcoinAddressAdmin(admin.ModelAdmin):
    list_display = ('address_name', 'address_no')
    
@admin.register(EthereumAddress)
class EthereumAddressAdmin(admin.ModelAdmin):
    list_display = ('address_name', 'address_no')
    
@admin.register(BinanceAddress)
class BinanceAddressAdmin(admin.ModelAdmin):
    list_display = ('address_name', 'address_no')

@admin.register(UsdtAddress)
class UsdtAddressAdmin(admin.ModelAdmin):
    list_display = ('address_name', 'address_no')
    
@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('package_name','package_details1','package_details2','package_details3','package_details4','package_range1','package_range2')