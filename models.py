from app import db
import enum

class Transporter(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    rating = db.Column(db.Numeric, nullable=False)
    bids = db.relationship('Bids')

class Shipper(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    jobs = db.relationship('Jobs')

class StatusEnum(enum.Enum):
    available = 1
    shipment = 2
    expired = 3

class Jobs(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    shipment_date = db.Column(db.Date, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    shipper_id = db.Column(db.Integer, db.ForeignKey('shipper.id'))
    expired_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum(StatusEnum))
    bids = db.relationship('Bids')

    def serialize(self):
        return {
            'id': self.id,
            'origin': self.origin,
            'destination': self.destination,
            'description': self.description,
            'shipment_date': self.shipment_date,
            'budget': self.budget,
            'expired_date': self.expired_date,
            'status': self.status.name
        }

class Bids(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    vehicle = db.Column(db.String, nullable=False)
    transporter_id = db.Column(db.Integer, db.ForeignKey('transporter.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    win_status = db.Column(db.Boolean, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'price': self.price,
            'vehicle': self.vehicle,
            'win_status': self.win_status
        }
