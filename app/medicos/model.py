from app.extensions import db
from enum import unique

class Medico(db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, primary_key = True)
    cpf = db.Column(db.Integer, nullable = False, unique = True)
    nome = db.Column(db.String(40), nullable = False)
    especialidade = db.Column(db.String(20), nullable = False)
    
