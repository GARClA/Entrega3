from app.extensions import db
from enum import unique
from app.association import association_table

class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key = True)
    cpf = db.Column(db.Integer, nullable = False, unique = True)
    nome = db.Column(db.String(40), nullable = False)

    consultas = db.relationship('Consulta')
    exames = db.relationship('Exame')
    receitas = db.relationship('Receita', secondary = association_table, backref = 'paciente')


    def json(self):
        return {"nome":self.nome,
                "cpf":self.cpf}