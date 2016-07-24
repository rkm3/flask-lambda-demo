# -*- coding: utf-8 -*-
"""
    Flask Demo - Hello World for AWS Lambda
    ~~~~~~
"""

import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


# create our little application :)
app = Flask(__name__)
# app = Flask('vanilla')
print app

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASK_SETTINGS', silent=True)


@app.route('/')
def index(): # fn name maps to template name
    return render_template('index.html')
