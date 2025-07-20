from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from accounts.forms import ProviderRegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.models import User


def welcome(request):
    return render(request, 'welcome.html')


def choose_role(request):
    return render(request, 'choose_role.html')


def route_by_role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'provider':
            return redirect('provider_login')
        elif role == 'client':
            return redirect('commuter_login')
    return redirect('welcome')  

def provider_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.role == 'provider':
            login(request, user)
            return redirect('provider_dash')  
        else:
            return render(request, 'provider_login.html', {'error': 'Invalid credentials or not a provider.'})

    return render(request, 'provider_login.html')

def provider_register(request):
    if request.method == 'POST':
        form = ProviderRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('provider_login')
    else:
        form = ProviderRegisterForm()
    return render(request, 'provider_reg.html', {'form': form})

@login_required
def provider_dashboard(request):
    return render(request, 'provider_dash.html')


@login_required
def scan_qr(request):
    if request.user.role != 'provider':
        return HttpResponse("Unauthorized", status=403)
    return render(request, 'scanner.html')  # Placeholder to trigger webcam

'''def provider_process_qr(request):
    if request.method == 'POST':
        commuter_id = request.POST.get('commuter_id')
        commuter = get_object_or_404(User, username=commuter_id)
        return render(request, 'provider_commuter_detail.html', {'commuter': commuter})

@login_required
def process_qr_result(request):
    scanned_username = request.session.get('scanned_username')
    message = request.session.pop('message', None)
    error = request.session.pop('error', None)

    commuter = None
    if scanned_username:
        try:
            commuter = User.objects.get(username=scanned_username, role='client')
        except User.DoesNotExist:
            commuter = None

    return render(request, 'process_qr.html', {
        'commuter': commuter,
        'message': message,
        'error': error
    }
    )

@login_required
def increment_bounty(request, user_id):
    try:
        commuter = get_object_or_404(User, id=user_id, role='client')

        # Increment wallet balance (customize amount as needed)
        commuter.wallet_balance = (commuter.wallet_balance or 0) + 10
        commuter.save()

        request.session['message'] = f"Bounty credited successfully to {commuter.username}'s wallet!"
    except Exception as e:
        request.session['error'] = "Something went wrong while crediting bounty."

    return redirect('process_qr_result')'''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

# Show commuter details after scanning
def process_qr(request):
    if request.method == 'POST':
        commuter_id = request.POST.get('commuter_id')
        # Now process this commuter_id as needed


# Increment bounty / wallet
def increment_bounty(request, commuter_id):
    if request.method == 'POST':
        commuter = get_object_or_404(User, id=commuter_id, role='client')
        commuter.wallet_balance += 5  # or whatever value you want
        commuter.save()
        request.session['message'] = "✅ Bounty credited!"
        return redirect('process_qr_result')
    return redirect('provider_dashboard')

# Final result page
def process_qr_result(request):
    commuter_id = request.session.get('commuter_id')
    message = request.session.pop('message', None)
    error = request.session.pop('error', None)
    commuter = None

    if commuter_id:
        try:
            commuter = User.objects.get(id=commuter_id, role='client')
        except User.DoesNotExist:
            error = "Commuter no longer exists."

    return render(request, 'process_qr_result.html', {
        'commuter': commuter,
        'message': message,
        'error': error,
    })

@login_required
def generate_qr(request):
    # your logic to generate QR
    return render(request, 'generate_qr.html')



