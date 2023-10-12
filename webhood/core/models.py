from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username
    
    

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.CharField(max_length=100)  # You can adjust the max_length as needed
    payment_description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    transaction_id = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

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
    id = models.IntegerField(primary_key=True)
    
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
    
    
    
    
# class Balance(models.Model):
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return str(self.amount)  # Ensure you return a string representation

#     @classmethod
#     def get_balance_for_user(cls, user):
#         try:
#             return cls.objects.get(user=user)
#         except cls.DoesNotExist:
#             # If there's no balance, create one with a default amount
#             return cls.objects.create(user=user)
    
    
    




    
# class ActivePackages(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     amount_invested = models.DecimalField(max_digits=100, decimal_places=2, default=0)
#     package_name = models.CharField(max_length=300)
    
#     def __str__(self):
#         return f"{self.user.username}'s Package"