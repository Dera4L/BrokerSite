from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

# Create your models here.


        
        
class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    
    def __str__(self):
        return f"{self.user.username}'s Balance"