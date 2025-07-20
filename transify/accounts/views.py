from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CommuterRegisterForm, ProviderRegisterForm
from .models import User, CommuterProfile
from django.contrib.auth import authenticate, login
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

@login_required
def provider_dashboard(request):
    return render(request, 'provider_dash.html')

def commuter_dashboard(request):
    if request.user.is_authenticated and request.user.role == 'client':
        bounty = request.user.commuterprofile.bounty
        return render(request, 'commuter_dashboard.html', {'bounty': bounty})
    return

def commuter_register(request):
    if request.method == 'POST':
        print("POST request received")
        form = CommuterRegisterForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save(commit=False)
            user.role = 'client'
            user.save()
            qr_data = f"{user.id}"
            qr_img = qrcode.make(qr_data)
            buffer = BytesIO()
            qr_img.save(buffer, format='PNG')
            file_name = f"qr_{user.username}.png"
            user.qr_code.save(file_name, ContentFile(buffer.getvalue()), save=True)

            CommuterProfile.objects.create(user=user)
            return redirect('commuter_login')
        else:
            print("Form errors:", form.errors)
    else:
        form = CommuterRegisterForm()
    return render(request, 'commuter_reg.html', {'form': form})



def commuter_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.role == 'client':
            login(request, user)
            return redirect('commuter_dashboard')
        else:
            return render(request, 'commuter_login.html', {'error': 'Invalid credentials or not a commuter.'})
    
    return render(request, 'commuter_login.html')


