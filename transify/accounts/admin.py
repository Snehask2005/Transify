from django.contrib import admin
from .models import CommuterProfile
from django.contrib.auth.admin import UserAdmin
from .models import User  # your custom user model

admin.site.register(User, UserAdmin)
