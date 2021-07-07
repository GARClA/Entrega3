from flask import request, Blueprint
from app.consultas.model import Consulta
from app.extensions import db

consulta_api = Blueprint('consulta_api', __name__)

@consulta_api.route('/consultas', methods = ['POST'])
def criar_consulta():
    if request.method == 'POST':
        dados = request.json
        data = dados.get('data')
        hora = dados.get('hora')
        tipo = dados.get('tipo')
        medico_id = dados.get('medico_id')
        paciente_id = dados.get('paciente_id')

        #Validando os dados
        if not isinstance(medico_id,int):
            return{'error':'ID do médico inválido'}
        if not isinstance(paciente_id,int):
            return{'error':'ID do paciente inválido'}
        if not isinstance(hora,str):
            return{'error':'Hora inválida'}
        if not isinstance(tipo,str):
            return{'error':'Tipo inválido'}
        if not isinstance(data,str):
            return{'error':'Data inválida'}

        consulta = Consulta(data = data, hora = hora, medico_id = medico_id, paciente_id = paciente_id, tipo = tipo)
        db.session.add(consulta)
        db.session.commit()

        return consulta.json(), 200