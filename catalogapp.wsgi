#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/CatalogApp/")

from CatalogApp import app as application
#from CatalogApp import catalogapp as application
#application.secret_key = 'grader'