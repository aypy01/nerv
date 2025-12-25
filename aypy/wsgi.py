import os
from django.core.wsgi import get_wsgi_application

# Make sure this points to your folder name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aypy.settings')

application = get_wsgi_application()