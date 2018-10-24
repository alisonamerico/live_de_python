"""O Flask usa sistema de roteamento simples, através de decorator.
Decorator é função
Onde a função def hello():
                :return hello
é chamada de view
"""
from flask import jsonify, render_template
"""Aplicando padrão de aplicações factories"""
def configure(app):

    @app.route('/')
    def hello():
        return 'Hello'

    @app.route('/api')
    def api():
        return jsonify(data={'name': 'Alison'})

    @app.route('/langs')
    def langs():
        languages = ['Python', 'Go', 'Lua', 'Rust']
        return render_template(
            'index.html', 
            title="The Best of Languages",
            languages=languages)
