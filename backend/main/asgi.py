"""
ASGI config for main project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from reports.fonts import load_fonts

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

load_fonts()

application = get_asgi_application()
