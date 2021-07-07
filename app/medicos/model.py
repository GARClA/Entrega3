from app.extensions import db
from enum import unique
from app.association import association_table

class Medico(db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, primary_key = True)
    cpf = db.Column(db.Integer, nullable = False, unique = True)
    nome = db.Column(db.String(40), nullable = False)
    especialidade = db.Column(db.String(20), nullable = False)
    
    consultas = db.relationship('Consulta')
    receitas = db.relationship('Receita', secondary = association_table, backref = 'medico')

    def json(self):
        return {"nome":self.nome,
                "cpf":self.cpf,
                "especialidade":self.especialidade}