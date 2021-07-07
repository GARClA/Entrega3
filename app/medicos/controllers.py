from flask import request, Blueprint
from app.medicos.model import Medico
from app.extensions import db

medico_api = Blueprint('medico_api', __name__)

@medico_api.route('/medico', methods = ['POST'])
def criar_medico():
    if request.method == 'POST':
        dados = request.json
        nome = dados.get('nome')
        cpf = dados.get('cpf')
        especialidade = dados.get('especialidade')

        #Validando os dados
        if not isinstance(nome,str):
            return{'error':'Nome do médico inválido'}
        if not isinstance(cpf,int):
            return{'error':'CPF do médico inválido'}
        if not isinstance(especialidade,str):
            return{'error':'Especialidade do médico inválida'}           

        medico = Medico(cpf = cpf, especialidade = especialidade, nome=nome)
        db.session.add(medico)
        db.session.commit()

        return medico.json(), 200