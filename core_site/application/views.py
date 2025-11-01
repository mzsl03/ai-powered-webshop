from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect


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
