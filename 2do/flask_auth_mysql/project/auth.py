#Importamos los módulos a usar de flask
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug import security
from flask import current_app
#Importamos los módulos de seguridad para las funciones hash
from werkzeug.security import generate_password_hash, check_password_hash
#Importamos el méodo login_user, logout_user, login_required de flask_login
from flask_security import login_required
from flask_security.utils import login_user,logout_user
#Importamos el modelo del usuario
from .models import User
#Importamos el objeto de la BD desde __init__
from . import db, userDataStore

auth = Blueprint('auth',__name__,url_prefix='/security')

@auth.route('/login_users')
def login_users():
    return render_template('/security/login_users.html')

@auth.route('/login_users', methods=['POST'])
def login_users_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    #Consultamos si existe un usuario ya registrado con el email.
    user = User.query.filter_by(email=email).first()

    #Verificamos si el usuario existe
    #Tomamos el password proporcionado por el usuario y lo hasheamos, 
    # y lo comparamos con el password de la base de datos.
    if not user:
        flash('El usuario y/o la contraseña son incorrectos')
        current_app.logger.error("El usuario y/o la contraseña son incorrectos")
        return redirect(url_for('auth.login_users')) 
    login_user(user, remember=remember)
    current_app.logger.debug("Se ha logueado")
    return redirect(url_for('main.profile'))

@auth.route('/register_users')
def register_users():
    return render_template('/security/register_user.html')

@auth.route('/register_users', methods=['POST'])
def register_users_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    #Consultamos si existe un usuario ya registrado con el email.
    user = User.query.filter_by(email=email).first()

    if user: #Si se encontró un usuario, redireccionamos de regreso a la página de registro
        flash('El correo electrónico ya existe')
        current_app.logger.error("El correo electrónico ya existe")
        return redirect(url_for('auth.register_users'))

    #Creamos un nuevo usuario con los datos del formulario.
    # Hacemos un hash a la contraseña para que no se guarde la versión de texto sin formato
    userDataStore.create_user(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.commit()
    current_app.logger.debug("Se ha registrado")
    return redirect(url_for('auth.login_users'))

@auth.route('/logout')
@login_required
def logout():
    #Cerramos la sessión
    logout_user()
    return redirect(url_for('main.index'))