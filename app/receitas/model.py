from app.extensions import db
from enum import unique
from app.association import association_table

class Receita(db.Model):
    __tablename__ = 'receita'
    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String(800), nullable = False)

    medicos = db.relationship('Medico', secondary = association_table, backref = 'receita')
    pacientes = db.relationship('Paciente', secondary = association_table, backref = 'receita')

    def json(self):
        return {"descricao":self.descricao}