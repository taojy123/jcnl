import sae
import sys,os
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'jcnl.settings'
application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())