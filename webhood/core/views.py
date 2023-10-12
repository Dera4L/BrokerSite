from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import *
import random
from decimal import Decimal
import uuid
import decimal


from .models import *

import random
# Create your views here.
from .forms import SignupForm


def index(request):
    return render(request, 'core/index.html')

@login_required
def dashboard(request):
    user = request.user
    balance = UserDetails.objects.get(user=user)        
    return render(request, 'core/dashboard.html',{
        'balance':balance,
    })



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/details/')

    form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def userdetails(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            date_of_birth = form.cleaned_data['date_of_birth']
            user = request.user
            
            UserDetails.objects.create(user=user, address=address, date_of_birth=date_of_birth)
            
            return redirect('/dashboard/')
    
    else:
        form = UserDetailsForm()
        
    return render(request, 'core/details.html',{
        'form':form
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
    user = request.user
    transactions = Transaction.objects.filter(user=user)
    # confirmed_transactions = Transaction.objects.filter(user=user, confirmed=True)

    # Calculate the balance by iterating over confirmed transactions
    # balance = UserDetails.objects.get(user=user).balance
    # for transaction in confirmed_transactions:
    #     balance += transaction.amount

    # # Update the user's UserDetails object with the calculated balance
    # user_details = get_object_or_404(UserDetails, user=user)
    # user_details.balance = balance
    # user_details.save()

    return render(request, 'core/transaction.html', {
        # 'confirmed_transactions': confirmed_transactions,
        'transactions': transactions
        # 'balance': balance,
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
    
    packages = Packages.objects.all()

    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            amount_to_invest = form.cleaned_data['amount']
            selected_package_name = request.POST.get('package_name')  # Assuming you have a package selection in your form
            selected_package = Packages.objects.get(package_name=selected_package_name)

            # Check if user's balance is sufficient
            if request.user.balance.amount >= amount_to_invest:
                # Update user's balance by subtracting the investment amount
                request.user.balance.amount -= amount_to_invest
                request.user.balance.save()

                # Create a record in the ActivePackages model
                active_package = ActivePackages(user=request.user, package=selected_package, amount_invested=amount_to_invest)
                active_package.save()

                # Redirect or show a success message
                # You can customize this part based on your application's requirements
                # Display an error message indicating insufficient balance
                # You can customize this part based on your application's requirements

    else:
        form = InvestmentForm()

    return render(request, 'core/packages.html', {
        'packages': packages,
        'form': form,
    })

@login_required
def packages(request):
    desired_name = "Bronze"
    user=request.user
    package1 = Packages.objects.filter(package_name=desired_name)
    if request.method == "POST":
        form = InvestmentForm(request.POST)
        if form.is_valid():
           amount_to_invest = form.cleaned_data['amount']
           selected_package = desired_name
           
               
            #    print(newbalance)
           
           
        #    print(selected_package,amount_to_invest,balance.amount)
           
        #    if balance.amount >= amount_to_invest:
        #        newbalance = balance.amount - amount_to_invest
        #        print(newbalance)
        else:
            return redirect('/transaction')
    else:
        form = InvestmentForm()
           
    
    
    
    return render(request, 'core/packages.html',{
        'package1':package1,
        'form':form
    })
    




























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

