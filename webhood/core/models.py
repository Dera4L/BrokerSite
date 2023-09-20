from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

# Create your models here.


        
        
class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    
    def __str__(self):
        return f"{self.user.username}'s Balance"
    
    

    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.CharField(max_length=100)  # You can adjust the max_length as needed
    payment_description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    transaction_id = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s fruit selection: {self.coin}"