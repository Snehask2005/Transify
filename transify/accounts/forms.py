
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User 

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProviderRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'full_name', 'phone', 'service_type', 'city']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'provider' 
        if commit:
            user.save()
        return user




class CommuterRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    wallet_address = forms.CharField(required=True, max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'full_name', 'phone', 'city', 'wallet_address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'client'  # mark as commuter
        user.full_name = self.cleaned_data['full_name']
        user.phone = self.cleaned_data['phone']
        user.city = self.cleaned_data['city']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            # Delay wallet_address until after profile is created by signal
            user.commuterprofile.wallet_address = self.cleaned_data['wallet_address']
            user.commuterprofile.save()

        return user