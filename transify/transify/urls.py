"""
URL configuration for transify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView, RedirectView
from accounts import urls
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import commuter_register, commuter_login_view, commuter_dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  
    path('', views.welcome, name='welcome'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('chose-role/', views.choose_role, name='choose_role'),
    path('rout-by-role/', views.route_by_role, name='route_by_role'),
    path('provider-login/', views.provider_login_view, name='provider_login'),
    path('provider/register/', views.provider_register, name='provider_reg'),
    path('provider/dashboard/', views.provider_dashboard, name='provider_dash'),
    path('provider/scan-qr/', views.scan_qr, name='scanner'),
    path('provider/process-qr/', views.process_qr, name='process_qr'),
    path('provider/qr/result/', views.process_qr_result, name='process_qr_result'),
    path('provider/increment/<int:user_id>/', views.increment_bounty, name='increment_bounty'),
    path('commuter/register/', commuter_register, name='commuter_register'),
    path('commuter-login/', commuter_login_view, name='commuter_login'),
    path('commuter/dashboard/', commuter_dashboard, name='commuter_dashboard'),
    path('generate-qr/', views.generate_qr, name='generate_qr'),
    path('process_qr/<int:commuter_id>/', views.process_qr, name='process_qr'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
