from app.extensions import db

class Exame(db.Model):
    __tablename__ = 'exame'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False)
    preco = db.Column(db.Float, nullable = False)
    data = db.Column(db.String(10), nullable = False)
    hora = db.Column(db.String(5), nullable = False)
    
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))


    def json(self):
        return {"nome":self.nome,
                "preco":self.preco,
                "data":self.data,
                "hora":self.hora,
                "paciente_id":self.paciente_id}