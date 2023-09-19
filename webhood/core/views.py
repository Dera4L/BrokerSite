from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Balance

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

def logout_view(request):
    logout(request)
    return redirect('/login/')


def generate_random(min_value, max_value):
    return random.randint(min_value, max_value)


@login_required
def make_payment(request):
    
    transfer_id = generate_random(100000000000, 50000000000000)
    
    
    return render(request, 'core/payment.html')



    