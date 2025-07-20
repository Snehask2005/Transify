

from django.urls import path
from . import views  # or specific views

urlpatterns = [
    path('provider/dashboard/', views.provider_dashboard, name='provider_dash'),
    
]
