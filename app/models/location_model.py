from app import db

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    # ---------------------------------------
    room = db.Column(db.String(80), nullable=False)
    adress = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Location {self.name}>'