from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
import random
import uuid


from .models import *

import random
# Create your views here.
from .forms import SignupForm


def index(request):
    return render(request, 'core/index.html')

@login_required
def dashboard(request):
    balance = Balance.objects.get(user=request.user)
    
        
    return render(request, 'core/dashboard.html',{
        'balance':balance,
    })



def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    
    else:
    
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def generate_random(min_value, max_value):
    return random.randint(min_value, max_value)


@login_required
def make_payment(request):
    
    transfer_id = generate_random(100000000000, 50000000000000)
    
    
    return render(request, 'core/payment.html')


def generate_transaction_id():
    #Generate a random 8-digit number
    random_number = random.randint(10000, 999999)
    
    #Generate a random 9-digit number
    random_number2 = random.randint(100000, 9999999)
    
    
    # Generate a uuid and convert it to a string
    unique_id = str(uuid.uuid4())
    
    transaction_id = f"{random_number}-{random_number2}-{unique_id}"
    
    return transaction_id



@login_required
def select_coin(request):
    
    
    bitcoinaddress = BitcoinAddress.objects.all()
    usdtaddress = UsdtAddress.objects.all()
    ethereumaddress = EthereumAddress.objects.all()
    binanceaddress = BinanceAddress.objects.all()

    return render(request, 'core/fruit_select.html',{
        'bitcoinaddress':bitcoinaddress,
        'usdtaddress': usdtaddress,
        'ethereumaddress': ethereumaddress,
        'binanceaddress': binanceaddress
        
    })


@login_required
def transaction(request):
    transactions = Transaction.objects.all()
    return render(request, 'core/transaction.html',{
        'transactions':transactions
    })



@login_required
def confirm(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            selected_coin = form.cleaned_data['coin']
            user = request.user  # Get the currently logged-in user
            description = form.cleaned_data['paymentdescription']
            amount = form.cleaned_data['amount']
            transaction_id = generate_transaction_id()
            Transaction.objects.create(user=user, coin=selected_coin, payment_description=description, amount=amount, transaction_id=transaction_id) # Save the selection
            return redirect('/dashboard/')
    else:
        form = TransactionForm()
    
    bitcoinaddress = BitcoinAddress.objects.all()
    usdtaddress = UsdtAddress.objects.all()
    ethereumaddress = EthereumAddress.objects.all()
    binanceaddress = BinanceAddress.objects.all()

    return render(request, 'core/confirm.html',{
        'form':form,
        'bitcoinaddress':bitcoinaddress,
        'usdtaddress': usdtaddress,
        'ethereumaddress': ethereumaddress,
        'binanceaddress': binanceaddress
        
    })
    

    
@login_required
def packages(request):
    return render(request, 'core/packages.html')



# def add_bitcoin_address(request):
#     if request.method == 'GET':
#         form = BitcoinAddressForm(request.POST)
        
#     if request.method == 'POST':
#         form = BitcoinAddressForm(request.POST)
#         if form.is_valid():
#             address_no = form.cleaned_data['address_no']
#             address_name = form.cleaned_data['address_name']
            
#             Address.objects.create(address_no=address_no, address_name=address_name)
#               # You can define an address list view
#             return redirect('/add/')
            
#     else:
#         form = BitcoinAddressForm()
#     return render(request, 'core/address.html', {'form': form})









# def select_coin(request):
#     if request.method == 'POST':
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             selected_coin = form.cleaned_data['coin']
#             address = TransactionForm.coin_choices_dict.get(selected_coin)
#             form.fields['address'].initial = address
#     else:
#         form = TransactionForm()

#     return render(request, 'core/fruit_select.html', {'form': form})

