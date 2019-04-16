import pytest
import os
from app import Shipper, Transporter, Jobs, Bids, app, db
from datetime import datetime


def conf_db(app):
    POSTGRES = {
        'user': 'postgres',
        'pw': 'postgres',
        'db': 'shipment_test',
        'host': 'localhost',
        'port': '5432',
    }
    if os.environ.get('CI'):
        POSTGRES['host'] = 'postgres'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


@pytest.fixture(scope='module')
def data_sort_jobs():
    jobs = []
    dates = [
        '2019-04-05', '2019-04-08', '2019-04-01', '2019-01-03', '2019-01-04',
        '2019-01-20', '2019-01-15',
    ]
    for index in range(len(dates)):
        jobs.append(Jobs(id = index+1, origin='JKT', destination='BDG', description='testdesc',
            shipment_date=dates[index], budget='1000000', expired_date='2025-01-01',
            status='available'
        ))
    return jobs

@pytest.fixture(scope='module')
def data_sort_bids():
    bids = []
    price = [
        10000, 2500, 1000, 5000, 7500
    ]
    for index in range(len(price)):
        bids.append(Bids(id = index+1, description='desc', price=price[index],
            vehicle='CDD', win_status=False
        ))
    return bids
