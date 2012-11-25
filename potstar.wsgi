import os
import sys

BASE_DIR = '/home/dommi/public_html/potstar'
DIR='live'
VIRTUAL_ENV_DIR = '/home/dommi/public_html/.virtualenvs/'

paths = [
    os.path.join(VIRTUAL_ENV_DIR, 'potstar', 'lib', 'python2.6', 'site-packages'),
    os.path.join(BASE_DIR, DIR, 'potstar'),
    os.path.join(BASE_DIR, DIR, 'potstar', 'store'),
    os.path.join(BASE_DIR, DIR, 'potstar', 'satchmo', 'apps'),
]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'store.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
