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

# from models import TrackRate, ExchangeRate, ExchangeRateData

@app.route("/")
def hello():
    return "Hello World!"