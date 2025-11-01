from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Products, Cart, Sales, Specs, Orders, UserInfo
from .forms.register_form import RegistrationForm

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Hibás felhasználónév vagy jelszó!'})
    return render(request, 'login.html')

def home(request):
    products = Products.objects.all()

    
    context = {
        'products': products,
    }

    return render(request, "index.html", context)

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        user = User.objects.create_user(
            last_name=form.cleaned_data['last_name'],
            first_name=form.cleaned_data['first_name'],
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        UserInfo.objects.create(
            user=user,
            address=form.cleaned_data['address'],
            birth_date=form.cleaned_data['birth_date'],
            phone_number=form.cleaned_data['phone_number'],
        )
        return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
