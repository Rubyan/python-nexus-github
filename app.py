#!/usr/bin/env python3

#######################################################################
# Author       : Johan van der Kuijl - johan.kuijl@alliander.com
# Version      : 0.0.6
# Date         : 2019-05-16
# Filename     : app.py
# Description  : A sample python webservice for Openshift to demonstrate Nexus
# Dependencies : see requirements.txt
# Versioning   : https://git.alliander.com/abr/openshift/python-nexus
# Input        :
# Output       :
# Configuration: All configuration is done in the file 'environment'
#
# Changes
# 0.1.0       : initial
#######################################################################

import os
import logging
import socket
from flask import Flask, jsonify
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(filename='environment'))

log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'host_name': HOST_NAME,
        'app_name': APP_NAME,
        'version': VERSION,
        'ip': IP,
        'port': PORT,
        'home_dir': HOME_DIR,
        'host': socket.gethostname()
    })

if __name__ == '__main__':
    VERSION = "0.1.0"

    app.secret_key = 'super secret key'

    HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS', 'localhost')
    APP_NAME = os.environ.get('OPENSHIFT_APP_NAME', 'flask')
    IP = os.environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1')
    PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8080))
    HOME_DIR = os.environ.get('OPENSHIFT_HOMEDIR', os.getcwd())

    app.run(host='0.0.0.0', port=PORT)
