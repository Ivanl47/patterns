from app import db

class Brocker(db.Model):
    __tablename__ = 'brokers'

    id = db.Column(db.Integer, primary_key=True)
    id_device = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # ---------------------------------------
    
    

    def __repr__(self):
        return f'<Brocker {self.name}>'