"""
Importando do módulo 'flask' a class 'Flask'

Criando uma instância do aplicativo 'Flask'. O __name__ é o nome do módulo no caso 'app
"""
import views
import contact
import db
import admin
from flask import Flask


"""Application factories - Função que recebe o aplicativo, altera a propriedade do aplicativo Flask"""


def create_app():
    app = Flask(__name__)

    # configurar extensoes
    db.configure(app)

    views.configure(app)

    admin.configure(app)

    contact.configure(app)

    # configurar variaveis
    app.config['SECRET_KEY'] = 'secret'
    return app




