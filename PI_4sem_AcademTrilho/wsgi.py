"""
WSGI config for PI_4sem_AcademTrilho project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PI_4sem_AcademTrilho.settings')

application = get_wsgi_application()
