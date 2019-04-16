from app import db

# class TrackRate(db.Model):
#     __tablename__ = 'trackrate'
#
#     id = db.Column(db.Integer, primary_key=True)
#     rate_id = db.Column(db.Integer, db.ForeignKey('exchangerate.id'), unique=True)
#     rate = db.relationship('ExchangeRate', foreign_keys=rate_id)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'rate': self.rate.serialize()
#         }
