from flask import Blueprint, render_template, request, abort, current_app

"""Criar o objeto de Blueprint"""
bp = Blueprint('contact', __name__, url_prefix='/contact')


@bp.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    # processar dados
    name = request.form.get('name')
    message = request.form.get('message')

    # validar
    if not name or not message:
        abort(400, 'Invalid message!')

    # banco de dados
    current_app.db.messages.insert_one({'name': name, 'message': message})

    return "Your message has been sent successfully!"



def configure(app):
    app.register_blueprint(bp)
