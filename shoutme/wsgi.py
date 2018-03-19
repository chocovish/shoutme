"""
WSGI config for shoutme project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoutme.settings")

application = get_wsgi_application()

# Heroku thing..!!

#from whitenoise.django import DjangoWhiteNoise
#pplication = DjangoWhiteNoise(application)
