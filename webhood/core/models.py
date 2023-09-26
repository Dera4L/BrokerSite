from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


    
    
    
    
    

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.CharField(max_length=100)  # You can adjust the max_length as needed
    payment_description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    transaction_id = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s fruit selection: {self.coin}"


class BitcoinAddress(models.Model):
    address_no = models.CharField(max_length=100, unique=True)
    address_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.address_name


class BinanceAddress(models.Model):
    address_no = models.CharField(max_length=100, unique=True)
    address_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.address_name


class EthereumAddress(models.Model):
    address_no = models.CharField(max_length=100, unique=True)
    address_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.address_name


class UsdtAddress(models.Model):
    address_no = models.CharField(max_length=100, unique=True)
    address_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.address_name


class Packages(models.Model):
    # owner = models.ForeignKey(Balance, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100, unique=True)
    package_details1 = models.CharField(max_length=400, default="features")
    package_details2 = models.CharField(max_length=400,default="features")
    package_details3 = models.CharField(max_length=400,default="features")
    package_details4 = models.CharField(max_length=400,default="features")
    
    
    
    package_range1 = models.IntegerField(
        validators=[MinValueValidator(1, message="must be greater than 1")]
    )
    package_range2 = models.IntegerField(
         validators=[
            MinValueValidator(1, message="Package range must be at least 1."),
            MaxValueValidator(10000000, message="Package range must be no more than 100.")
        ]
    )
    
    
    
    
class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    package = models.ForeignKey(Packages, related_name='my_packages', on_delete=models.CASCADE,default="1")

    def __str__(self):
        return f"{self.user.username}'s Balance"
    
    def can_purchase(self, package_obj):
        return self.amount >= package_obj.package_range1




    
class ActivePackages(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    package_name = models.ForeignKey(Packages, related_name='active_package', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}'s Package"