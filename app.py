from flask import Flask, request, jsonify, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'shipment',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)

from models import Shipper, Transporter, Jobs, Bids


# Sort data using bubble sort
def sort_job(arr):
    n = len(arr)

    while True:
        swapped = False
        for i in range(1, n):
            if (arr[i - 1].shipment_date > arr[i].shipment_date):
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                swapped = True
        if not swapped:
            break

def sort_bid(arr):
    n = len(arr)

    while True:
        swapped = False
        for i in range(1, n):
            if (arr[i - 1].price > arr[i].price):
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                swapped = True
        if not swapped:
            break

@app.route("/job", methods=['GET'])
def job_data():
    sort_param = request.args.get('order_by')
    jobs = Jobs.query.all()
    if sort_param == 'shipment_date':
        sort_job(jobs)
    return jsonify([e.serialize() for e in jobs])

@app.route("/bid", methods=['GET'])
def bid_data():
    sort_param = request.args.get('order_by')
    bids = Bids.query.all()
    if sort_param == 'price':
        sort_bid(bids)
    return jsonify([e.serialize() for e in bids])
