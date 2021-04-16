
from flask import Blueprint, render_template
from flask_security import current_user
from flask_security.decorators import roles_required
from . import db

main = Blueprint('main',__name__)

#Definimos la ruta a la página pricipal
@main.route('/')
def index():
    return render_template('index.html')

#Definimos la ruta a la página de perfil
@main.route('/profile')
@roles_required('admin')
def profile():
    return render_template('profile.html', name=current_user.name)