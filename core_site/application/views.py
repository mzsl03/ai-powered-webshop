from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .forms.register_form import RegistrationForm
from .forms.user_update_form import UserUpdateForm
from .models import Products, Cart, Sales, Specs, Orders, UserInfo, OrderItem
from django.contrib.auth.decorators import login_required
from support_files.add_prod import ProductForm
from support_files.add_specs import SpecsForm
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.http import require_POST





def login(request):
    error = ""

    if request.method == 'POST':
        username_raw = request.POST.get('username')
        password_raw = request.POST.get('password')

        username = username_raw.strip() if username_raw else ""
        password = password_raw.strip() if password_raw else ""

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Sikeresen bejelentkezett {username}!")
            return redirect('home')
        else:
            error = 'Hibás felhasználónév vagy jelszó!'
            if username == "" or password == "":
                error = "Minden mező kitöltése kötelező!"
            context = {
                "error": error,
                "request": request
            }
        return render(request, 'login.html', context)

    return render(request, 'login.html', {'error': error})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
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
            messages.success(request, 'Sikeres regisztráció')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

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

@login_required(login_url='/')
def add_product(request):
    all_categories = Products.objects.values_list("category", flat=True).distinct()

    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
                 
            if product.category == 'Telefon':
                messages.success(request, f"{product.name} sikeresen létrehozva. Add meg a specifikációs adatokat!")
                return redirect('add_specs', product_id=product.id)
            else:
                messages.success(request, f"{product.name} sikeresen létrehozva!")
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


@login_required(login_url='/')
def product_detail(request, name, color):
    product = get_object_or_404(Products, name=name)
    specs = None
    if product.category != "Tartozék":
        specs = Specs.objects.filter(product=product).first()

   # phoneshop_user = request.user.phoneshop_user

    if request.method == 'POST':
        form = SpecsForm(request.POST, instance=specs)
        if form.is_valid():
            form.save()
            available_count = len(specs.storage) * len(specs.product.colors)
            product.stock = [10] * available_count
            product.save()
            return redirect('home')
    else:
        form = SpecsForm(instance=specs)


    return render(request, 'item_view.html', {
        'product': product,
        'form': form,
        'color': color
    })

@login_required(login_url='/')
def cart(request):
    user_id = request.user.id

    user_products = Cart.objects.filter(user_id=user_id)

    total_sum = sum(item.price for item in user_products)

    context = {
        "user_id": user_id,
        "products": user_products,
        "sum": total_sum
    }

    return render(request, "cart.html", context)

@require_POST
@login_required
def delete_cart_item(request, item_id):
    try:
        item = Cart.objects.get(id=item_id, user=request.user)
        item.delete()


        user_products = Cart.objects.filter(user_id=request.user)
        new_total_sum = sum(item.price for item in user_products)
        return JsonResponse({'success': True, "new_total": new_total_sum})
    except Cart.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)

@login_required(login_url='/')
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "A profilod sikeresen frissült!")
            return redirect('home')
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'update_user.html', {'form': form, 'user': user})


@login_required(login_url='/')
def user_order(request):
    user = request.user
    processing = Orders.objects.filter(user=user, status='feldolgozás_alatt')
    delivered = Orders.objects.filter(user=user, status='kiszállítva')
    deleted = Orders.objects.filter(user=user, status='törölve')
    return render(request, 'user_order.html', {'processing': processing, 'delivered': delivered, 'deleted': deleted, })

@login_required
def all_user_order(request):
    orders = Orders.objects.all().order_by('-order_time')
    return render(request, 'list_orders.html', {'orders': orders})



@login_required(login_url='/')
def add_to_cart(request, product_id):
    # Prevent superusers from adding to cart
    if request.user.is_superuser:
        return redirect('home')

    # Access UserInfo if needed
    phoneshop_user = request.user.phoneshop_user
    print("Adding to cart for:", phoneshop_user.id)

    product = get_object_or_404(Products, id=product_id)
    color = request.GET.get("color") or request.POST.get("color")
    storage = request.GET.get('storage')

    # Validate color
    if not color or color.strip().lower() not in [c.lower() for c in product.colors]:
        color = 'black'

    if not storage:
        storage = 128

    # Check if item already in cart
    is_in_cart = Cart.objects.filter(
        user=request.user,
        product=product,
        color=color,
        storage=storage
    ).exists()

    if not is_in_cart:
        Cart.objects.create(
            user=request.user,   # Cart expects User, not UserInfo
            product=product,
            quantity=1,
            price=product.price,
            color=color,
            storage=storage
        )
    else:
        # If already in cart, increment quantity
        cart_item = Cart.objects.get(
            user=request.user,
            product=product,
            color=color,
            storage=storage
        )
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

@login_required(login_url='/')
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.warning(request, "A kosár üres, nincs mit leadni.")
        return redirect("cart")

    order = Orders.objects.create(
        user=request.user,
        status="feldolgozás_alatt",
        order_time=timezone.now()
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            color=item.color,
            storage=item.storage,
            price=item.price * item.quantity,
        )

    cart_items.delete()

    messages.success(request, "Rendelésed sikeresen leadva!")

    return redirect("user_order", user_id=request.user.id)