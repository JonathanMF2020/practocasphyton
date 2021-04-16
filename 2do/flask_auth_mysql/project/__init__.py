import os
from flask import Flask
from flask_security import current_user, Security,SQLAlchemyUserDatastore, utils
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from werkzeug.security import generate_password_hash, check_password_hash


#Creamos una instancia de SQLAlchemy
db = SQLAlchemy()
from .models import User, Role,UserAdmin,RoleAdmin
userDataStore = SQLAlchemyUserDatastore(db,User,Role)

#Método de inicio de la aplicación
def create_app():
    app = Flask(__name__)  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask_admin3'
    app.logger.debug("Conecto a la base de datos")
    app.config['SECURITY_PASSWORD_SALT'] = 'thissecretssalt'
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    db.init_app(app)
    @app.before_first_request
    def create_all():
        app.logger.debug("Genero tablas en caso de necesitarlo")
        db.create_all()
        user_datastore.find_or_create_role(name='admin', description='Administrator')
        user_datastore.find_or_create_role(name='end-user', description='End user')
        if not user_datastore.get_user('someone@example.com'):
            user_datastore.create_user(email='someone@example.com', password=generate_password_hash("usuario", method='sha256'),name="Prueba")
        if not user_datastore.get_user('admin@example.com'):
            user_datastore.create_user(email='admin@example.com', password=generate_password_hash("admin", method='sha256'),name="Admin")
        db.session.commit()
        user_datastore.add_role_to_user('someone@example.com', 'end-user')
        user_datastore.add_role_to_user('admin@example.com', 'admin')
        db.session.commit()
    admin = Admin(app)
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(RoleAdmin(Role, db.session))
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.logger.debug("Inicio la aplicacion")
    return app


