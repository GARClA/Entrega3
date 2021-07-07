from app.extensions import db

association_table = db.Table('association', db.Model.metadata, 
                                db.Column('medico', db.Integer, db.ForeignKey('medico.id')),
                                db.Column('receita',db.Integer, db.ForeignKey('receita.id')))