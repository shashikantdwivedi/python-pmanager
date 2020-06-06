#!/home/ubuntu/miniconda3/envs/pmanager/bin
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/ubuntu/pmanager/pmanager/")

from app import app as application
# TODO - Replace SECRET-KEY with your application secret key
application.secret_key = 'SECRET-KEY'
