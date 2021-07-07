from flask import request, Blueprint
from app.receitas.model import Receita
from app.extensions import db

receita_api = Blueprint('receita_api', __name__)

@receita_api.route('/receitas', methods = ['POST'])
def criar_receita():
    if request.method == 'POST':
        dados = request.json
        descricao = dados.get('descricao')

        #Validando os dados
        if not isinstance(descricao,str):
            return{'error':'Descrição inválida'}        

        receita = Receita(descricao = descricao)
        db.session.add(receita)
        db.session.commit()

        return receita.json(), 200