import os
from django.core.wsgi import get_wsgi_application

# Устанавливаем настройки Django для WSGI
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dds_project.settings")

application = get_wsgi_application()
