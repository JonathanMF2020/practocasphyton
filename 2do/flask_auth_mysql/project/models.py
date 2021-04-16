from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin,RoleMixin,utils,current_user
from flask_admin.contrib import sqla
from wtforms.fields import PasswordField

#db = SQLAlchemy()

users_roles = db.Table('users_roles',
    db.Column('userId',db.Integer,db.ForeignKey('user.id'))  ,
    db.Column('roleId',db.Integer,db.ForeignKey('role.id'))                    
)

class User(UserMixin, db.Model):
    """User account model."""
    
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship('Role',
        secondary=users_roles,
        backref=db.backref('user',lazy='dynamic')                        
    )
    

class Role(RoleMixin, db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

class UserAdmin(sqla.ModelView):
    column_exclude_list = ('password',)
    form_excluded_columns = ('password',)
    column_auto_select_related = True
    def is_accessible(self):
        return current_user.has_role('admin')
    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.password2 = PasswordField('New Password')
        return form_class
    def on_model_change(self, form, model, is_created):
        if len(model.password2):
            model.password = utils.encrypt_password(model.password2)


class RoleAdmin(sqla.ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')
