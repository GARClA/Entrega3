from flask import request, Blueprint
from app.pacientes.model import Paciente
from app.extensions import db

paciente_api = Blueprint('paciente_api', __name__)

@paciente_api.route('/pacientes', methods = ['POST'])
def criar_paciente():
    if request.method == 'POST':
        dados = request.json
        nome = dados.get('nome')
        cpf = dados.get('cpf')
        temperatura = dados.get('temperatura')
        pressao = dados.get('pressao')

        #Validando os dados
        if not isinstance(nome,str):
            return{'error':'Nome do paciente inválido'}
        if not isinstance(cpf,int):
            return{'error':'CPF do paciente inválido'}     
        if not isinstance(temperatura,int):
            return{'error':'Temperatura do paciente inválida'}  
        if not isinstance(pressao,str):
            return{'error':'Pressão do paciente inválida'}   

        paciente = Paciente(cpf = cpf, nome=nome, temperatura = temperatura, pressao = pressao)
        db.session.add(paciente)
        db.session.commit()

        return paciente.json(), 200