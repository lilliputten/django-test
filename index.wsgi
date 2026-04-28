# -*- coding: utf-8 -*-
# ex: set ft=python :

import os
import sys
import time
import traceback
import signal
from pathlib import Path

import logging

# @see https://docs.djangoproject.com/en/5.1/intro/tutorial02/

# App root path
rootPath = os.path.dirname(os.path.abspath(__file__))

# Detect home path...
home = str(Path.home())

logging.basicConfig(filename=f'{rootPath}/.debug.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# NOTE: activating a proper venv in the UWSGI Emperor
# # activate_this = f"{rootPath}/../../venv/bin/activate_this.py"
# # activate_this = home + '/.venv-py3.11-django-5/bin/activate_this.py'
# # activate_this = home + '/.venv-py3.13-django-6/bin/activate_this.py'
# activate_this = home + '/.venv-py3.11-django-5/bin/activate_this.py'
#
# with open(activate_this) as f:
#     code = compile(f.read(), activate_this, 'exec')
#     exec(code, dict(__file__=activate_this))

sys.path.insert(1, rootPath)

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

from django.core.wsgi import get_wsgi_application

try:
    application = get_wsgi_application()
except RuntimeError:
    traceback.print_exc()
    os.kill(os.getpid(), signal.SIGINT)
    time.sleep(2.5)
