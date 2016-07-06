"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os,sys


mysite= os.path.dirname(__file__)
project = os.path.dirname(mysite)
#python_home = 'd:\\python27'

sys.path.append(mysite)
sys.path.append(project)
#sys.path.append(python_home)

activate_env_file = os.path.join(project,'django_env','Scripts','activate_this.py')

execfile(activate_env_file, dict(__file__=activate_env_file))

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
