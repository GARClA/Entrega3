from app.extensions import db
from enum import unique

class Receita(db.Model):
    __tablename__ = 'receita'
    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String(800), nullable = False)