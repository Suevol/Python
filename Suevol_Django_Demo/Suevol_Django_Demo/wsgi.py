import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Suevol_Django_Demo.settings")

application = get_wsgi_application()
