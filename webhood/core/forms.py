from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    email =  forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    password1 =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    password2 =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confrim Password',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    
    



class UserDetailsForm(forms.Form):
    address =  forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'address',
    'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    
    date_of_birth =  forms.DateField(widget=forms.DateInput(attrs={
    'placeholder': 'Date of Birth',
    'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    
        
        




class LoginForm(AuthenticationForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    password =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))


class PaymentForm(AuthenticationForm):
    amount =  forms.FloatField(widget=forms.TextInput(attrs={
        'placeholder': 'Input Amount',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    
    paymentdescription =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Description',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    
    




class TransactionForm(forms.Form):
    coin_choices = (
        ('BTC', 'Bitcoin - BTC'),
        ('ETH', 'Ethereum - ETH'),
        ('LTC', 'Litecoin - LTC'),
        ('USDT', 'Tether- USDT'),
        # Add more coins as needed
    )
    coin = forms.ChoiceField(choices=coin_choices, label='Select Coin', widget=forms.Select(attrs={
        'class': 'form-select',  # Apply Bootstrap's form-select class for styling
        'id': 'coin-select',  # Unique ID for this field
    }))
    paymentdescription =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Description',
        'class' : 'form-control',
        'id':'floatingInputValue',
    }))
    amount =  forms.FloatField(widget=forms.TextInput(attrs={
        'placeholder': 'Input Amount',
        'class' : 'form-control',
        'id':'floatingInputValue',
    }))
    
    coin_choices_dict = {
        'BTC': 'BTC_ADDRESS',
        'ETH': 'ETH_ADDRESS',
        'LTC': 'LTC_ADDRESS',
        'USDT': 'USDT_ADDRESS',
        # Add more coin addresses as needed
    }
    
    
    
class BuyItemForm(forms.Form):
    amount = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': 'Input Amount',
        'class':'form-control',
        'id': 'floatingInputValue',
    }))

    

class BitcoinAddressForm(forms.Form):
    address_no = forms.CharField(max_length=100, label='Coin Address')
    address_name = forms.CharField(max_length=100, label='Address name')
    


class InvestmentForm(forms.Form):
    amount = forms.DecimalField(label='Amount to Invest')