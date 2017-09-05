#!/usr/bin/python
import sys
import logging

activate_this = '/home/grader/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/CatalogApp/")

from CatalogApp import app as application
application.secret_key = 'super_secret_key'
#from CatalogApp import catalogapp as application
#application.secret_key = 'grader'