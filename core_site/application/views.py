from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import get_object_or_404, render, redirect
from .models import Products, Cart, Sales, Specs, Orders
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from support_files.add_prod import ProductForm
from support_files.add_specs import SpecsForm
from django.contrib import messages
from django.utils import timezone




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
        form = {
            'last_name': request.POST.get('last_name', '').strip(),
            'first_name': request.POST.get('first_name', '').strip(),
            'username': request.POST.get('username', '').strip(),
            'address': request.POST.get('address', '').strip(),
            'password': request.POST.get('password', '').strip(),
        }
        password = form['password']

        if not all([form['last_name'], form['first_name'], form['username'], password, form['address']]):
            return render(request, 'register.html', {'error': 'Minden mező kitöltése kötelező!', 'form': form})
        if len(password) < 8:
            return render(request, 'register.html', {'error': 'A jelszónak legalább 8 karakter hosszúnak kell lennie!', 'form': form})

        return render(request, 'register.html', {'success': 'Sikeres regisztráció!', 'form': form, 'redirect': True})

    return render(request, 'register.html')


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
                return redirect('add_specs', product_id=product.id)
            else:
                return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {
        'form': form,
        "categories": all_categories
    })

@login_required(login_url='/')
def add_specs(request, product_id):
    if not request.user.is_superuser:
        return redirect('home')
    product = get_object_or_404(Products, id=product_id)
    specs, created = Specs.objects.get_or_create(product=product,
                                                 defaults={
                                                     "weight": 0,
                                                     "battery": 0,
                                                     "release_date": timezone.now(),
                                                 })

    if request.method == 'POST':
        form = SpecsForm(request.POST, instance=specs)
        if form.is_valid():
            form.save()
            available_count = len(specs.storage) * len(specs.product.colors)
            product.stock =  [10] * available_count
            product.save()
            return redirect('home')
    else:
        form = SpecsForm(instance=specs)

    return render(request, 'add_specs.html', {'form': form, 'product': product})