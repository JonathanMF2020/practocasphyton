from flask import Blueprint, render_template,request,redirect,url_for
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
from . import db
import os
from .models import Producto

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@roles_required('user')
@main.route('/profile')
def profile():
    productos = db.session.query(Producto).all()
    for role in current_user.roles:
        if(role.name == 'admin'):
            return render_template('profile_admin.html', name=current_user.name,productos=productos)
        else:
            return render_template('profile.html', name=current_user.name,productos=productos)
        
@roles_required('admin')
@main.route('/delete_product', methods=['GET'])
def delete_product():
   if request.method == "GET":
       id = request.args.get('id')
       producto = db.session.query(Producto).filter(Producto.id == id).first()
       db.session.delete(producto)
       db.session.commit()
       productos = db.session.query(Producto).all()
       return render_template('profile_admin.html', name=current_user.name,productos=productos)
   
   
@roles_required('user')
@main.route('/formulario', methods=['GET'])
def formulario():
   if request.method == "GET":
       return render_template('formulario.html')
   
   
@roles_required('admin')
@main.route('/edit_product', methods=['GET', 'POST'])
def edit_product():
   if request.method == "GET":
       id = request.args.get('id')
       producto = db.session.query(Producto).filter(Producto.id == id).first()
       return render_template("edit_product.html",producto=producto)
   else:
       id = request.form.get("id")
       file1 = request.files['imagen']
       nombre = request.form.get("nombre")
       descripcion = request.form.get("descripcion")
       precio = request.form.get("precio")
       producto = db.session.query(Producto).filter(Producto.id == id).first()
       producto.nombre = nombre
       producto.descripcion = descripcion
       producto.precio = precio
       db.session.add(producto)
       db.session.commit()
       productos = db.session.query(Producto).all()
       return render_template('profile_admin.html',productos=productos)
       
@roles_required('admin')
@main.route('/add_product', methods=['GET', 'POST'])
def add_product():
   if request.method == "GET":
       return render_template("add_product.html")
   else:
       file1 = request.files['imagen']
       nombre = request.form.get("nombre")
       descripcion = request.form.get("descripcion")
       precio = request.form.get("precio")
       producto = Producto(nombre=nombre,descripcion=descripcion,precio=precio,foto=file1.filename)
       db.session.add(producto)
       path = os.path.join("project/static/imagenes/upload/", file1.filename)
       file1.save(path)
       db.session.commit()
       productos = db.session.query(Producto).all()
       return render_template('profile_admin.html',productos=productos)
   
