# accounts/views.py

from django.shortcuts import render, redirect
from .models import Client


# ===============================
# CLIENT LOGIN
# ===============================
def login_view(request):

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        try:
            client = Client.objects.get(user_id=user_id, password=password)

            # Save session
            request.session['client_id'] = client.id

            return redirect('client_dashboard')

        except Client.DoesNotExist:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'accounts/login.html')


# ===============================
# CLIENT DASHBOARD
# ===============================
def client_dashboard(request):

    if not request.session.get('client_id'):
        return redirect('login')

    return render(request, 'accounts/dashboard.html')


# ===============================
# CLIENT LOGOUT
# ===============================
def logout_view(request):
    request.session.flush()
    return redirect('login')