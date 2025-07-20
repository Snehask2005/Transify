from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import qrcode 
from io import BytesIO
from django.core.files import File

class User(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Commuter'),
        ('provider', 'Transport Provider'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    service_type = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    wallet_balance = models.IntegerField(default=0)
    wallet_address = models.CharField(max_length=255, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def generate_qr_code(self):
        data = f"http://127.0.0.1:8000/process_qr/{self.id}/"
        qr = qrcode.make(data)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        self.qr_code.save(f'qr_{self.username}.png', File(buffer), save=False)

class CommuterProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bounty = models.PositiveIntegerField(default=0)
    wallet_address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"