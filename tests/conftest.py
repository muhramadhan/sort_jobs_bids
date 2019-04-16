import pytest
import os
from app import ExchangeRateData, TrackRate, ExchangeRate, app, db
from datetime import datetime


def conf_db(app):
    POSTGRES = {
        'user': 'postgres',
        'pw': 'postgres',
        'db': 'forex_test',
        'host': 'localhost',
        'port': '5432',
    }
    if os.environ.get('CI'):
        POSTGRES['host'] = 'postgres'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
