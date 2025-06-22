from app import db

class Device(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    # data_id = db.Column(db.Integer, db.ForeignKey('device_data.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    # ---------------------------------------
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(80), nullable=False)
    topic = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Device {self.name}>'