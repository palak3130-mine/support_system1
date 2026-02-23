"""
ASGI config for config project.

This file exposes the ASGI callable as a module-level variable named "application".
Used for async servers like Daphne / Uvicorn.
"""

import os
from django.core.asgi import get_asgi_application

# Set default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# ASGI application instance
application = get_asgi_application()