from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms.register_form import RegistrationForm
from .models import Products, Cart, Sales, Specs, Orders, UserInfo
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from support_files.add_prod import ProductForm
from django.contrib import messages



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


@login_required(login_url='/')
def home(request):
    products = Products.objects.all()

    all_categories = Products.objects.values_list("category", flat=True).distinct()

    products, categories, filters= sort_product(request, products)

    context = {
        'products': products,
        'categories': categories,
        'allCategory': all_categories,
        "filters": filters
    }

    return render(request, "index.html", context)


def sort_product(request, products):
    name = request.GET.get('name')
    category = request.GET.get('category')
    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')

    filters = {
        "name": name,
        "category": category,
        "min_price": min_price,
        "max_price": max_price,
    }

    if name:
        name = name.replace(" ", "").lower()
        products = [p for p in products if name in p.name.replace(" ", "").lower()]


    if category and category != "all":
        products = [p for p in products if p.category == category]

    if min_price:
        products = [p for p in products if p.price >= int(min_price)]

    if max_price:
        products = [p for p in products if p.price <= int(max_price)]


    categories = Products.objects.values_list('category', flat=True).distinct()

    return products, categories, filters
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

@login_required(login_url='/')
def add_product(request):
    all_categories = Products.objects.values_list("category", flat=True).distinct()

    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            category = form.cleaned_data["category"]

            if Products.objects.filter(name=name, category=category).exists():
                messages.add_message(request, messages.ERROR, "Ez a termék már létezik!")
                return render(request, 'add_product.html', {
                    'form': form,
                    "categories": all_categories
                })

            product = form.save()
            if product.category == 'Telefon':
                return redirect('edit_specs', product_id=product.id)
            else:
                return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {
        'form': form,
        "categories": all_categories
    })
