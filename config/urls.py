"""
Main URL routing for Support System project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Django admin backend
    path('admin/', admin.site.urls),

    # Client portal
    path('', include('accounts.urls')),

    # Ticket system
    path('tickets/', include('tickets.urls')),

    # Staff / Admin dashboard
    path('staff/', include('dashboard.urls')),
]