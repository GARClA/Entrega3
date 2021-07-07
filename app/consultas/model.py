from app.extensions import db

class Exame(db.Model):
    __tablename__ = 'exame'
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10), nullable = False)
    hora = db.Column(db.String(5), nullable = False)

    #Pensar em usar Datetime no lugar de String
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))