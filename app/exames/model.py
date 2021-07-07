from app.extensions import db
from enum import unique

class Exame(db.Model):
    __tablename__ = 'exame'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False,  unique = True)
    preco = db.Column(db.Float, nullable = False)
    