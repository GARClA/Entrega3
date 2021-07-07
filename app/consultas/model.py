from app.extensions import db

class Consulta(db.Model):
    __tablename__ = 'consulta'
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10), nullable = False)
    hora = db.Column(db.String(5), nullable = False)
    tipo = db.Column(db.String(20), nullable = False)

    #Pensar em usar Datetime no lugar de String
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))

    def json(self):
        return {"data":self.data,
                "hora":self.hora,
                "tipo":self.tipo,
                "medico_id":self.medico_id,
                "paciente_id":self.paciente_id}