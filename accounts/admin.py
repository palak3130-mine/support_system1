# accounts/admin.py

from django.contrib import admin
from .models import Client


# Register Client model in admin panel
admin.site.register(Client)