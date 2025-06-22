from app import db

class DeviceData(db.Model):
    __tablename__ = 'device_data'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)
    # ---------------------------------------
    secure_status = db.Column(db.Boolean, nullable=False, default=False)
    temprature = db.Column(db.Float, nullable=True)
    humidity = db.Column(db.Float, nullable=True)
    time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<DeviceData {self.device_id} {self.time} {self.temprature}>'