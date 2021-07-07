from app.extensions import db

class Exame(db.Model):
    __tablename__ = 'exame'
    id = db.Column(db.Integer, primary_key = True)