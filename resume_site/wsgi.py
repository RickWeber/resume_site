"""
WSGI config for resume_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_site.settings')
<<<<<<< HEAD
os.environ['HTTPs'] = "on"
=======
os.environ['HTTPS'] = "on"
>>>>>>> 61198899668a98a4b1a45fa8d423b95ca16a3c52

application = get_wsgi_application()
