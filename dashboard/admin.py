# dashboard/admin.py

from django.contrib import admin
from .models import Staff


# ===============================
# STAFF ADMIN PANEL CONFIG
# ===============================
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):

    list_display = ('name', 'username', 'speciality', 'email')

    search_fields = ('name', 'username', 'email')

    list_filter = ('speciality',)