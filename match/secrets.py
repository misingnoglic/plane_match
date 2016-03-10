__author__ = 'arya'
import os
amadeus_key = str(os.environ.get('AMADEUS_KEY', 'fail'))
sendgrid_user = str(os.environ.get('SENDGRID_USER', 'fail'))
sendgrid_pass = str(os.environ.get('SENDGRID_PASS', 'fail'))