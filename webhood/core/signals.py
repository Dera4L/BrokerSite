# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User


# from .models import Balance

# @receiver(post_save, sender=User)
# def create_balance(sender, instance, created, **kwargs):
#     if created:
#         Balance.objects.create(user=instance)
        
# @receiver(post_save, sender=User)
# def save_user_balance(sender, instance, **kwargs):
#     instance.balance.save()