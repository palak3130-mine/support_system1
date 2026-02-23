"""
WSGI config for config project.

This exposes the WSGI callable as "application".
Used for deployment with servers like Gunicorn.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# WSGI application instance
application = get_wsgi_application()