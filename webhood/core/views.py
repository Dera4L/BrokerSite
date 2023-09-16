from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
from .forms import SignupForm



def index(request):
    return render(request, 'core/index.html')

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')



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