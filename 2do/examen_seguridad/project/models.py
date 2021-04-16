from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin,RoleMixin

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
    
class Producto(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(90))
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.Float())
    foto = db.Column(db.String(255))
    
