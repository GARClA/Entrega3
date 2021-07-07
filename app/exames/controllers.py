from flask import request, Blueprint
from app.exames.model import Exame
from app.extensions import db

exame_api = Blueprint('exame_api', __name__)

@exame_api.route('/exames', methods = ['POST'])
def criar_exame():
    if request.method == 'POST':
        dados = request.json
        nome = dados.get('nome')
        preco = dados.get('preco')
        data = dados.get('data')
        hora = dados.get('hora')
        paciente_id = dados.get('paciente_id')

        #Validando os dados
        if not isinstance(nome,str):
            return{'error':'Nome do exame inválido'}
        if not isinstance(paciente_id,int):
            return{'error':'ID do paciente inválido'}
        if not isinstance(preco,float):
            return{'error':'Preço inválido'}           
        if not isinstance(hora,str):
            return{'error':'Hora inválida'}
        if not isinstance(data,str):
            return{'error':'Data inválido'}

        exame = Exame(data = data, hora = hora, preco = preco, paciente_id = paciente_id, nome=nome)
        db.session.add(exame)
        db.session.commit()

        return exame.json(), 200