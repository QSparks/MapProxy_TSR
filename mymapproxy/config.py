# WSGI module for use with Apache mod_wsgi or gunicorn

# # uncomment the following lines for logging
# # create a log.ini with `mapproxy-util create -t log-ini`
# from logging.config import fileConfig
# import os.path
# fileConfig(r'/PATH/mymapproxy/log.ini', {'here': os.path.dirname(__file__)})

from mapproxy.wsgiapp import make_wsgi_app

application = make_wsgi_app(r"/app/mapproxy.yaml", reloader=True)
