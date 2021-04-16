from flask import Flask, render_template
from flask import request
import form 
app=Flask(__name__)



@app.route('/')
def index():
    nombre = "Jonathan"
    lista = ["Español","Ingles","Matematicas","Español"]
    return render_template("index.html",nombre=nombre,lista=lista)

@app.route("/sum",methods=['GET','POST'])
def sum():
     if request.method == "POST":
         numero1 = request.form.get("numero1")
         numero2 = request.form.get("numero2")
         resultado = int(numero1)+int(numero2)
         return "<h1>Resultado es {}</h1>".format(resultado)
     else:
         return '''<form action="/sum" method="POST"> 
            <label>Numero 1<label><br>
            <input type="number" name="numero1" id="numero1"><br>
            <label>Numero 2<label><br>
            <input type="number" name="numero2" id="numero2"><br>
            <input type="submit">
        </form>
     '''

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/formulario2',methods=['GET','POST'])
def formulario2():
    login_form = form.LoginForm(request.form)
    print(login_form.username.data)
    return render_template('formulario2.html',formulario=login_form)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/operaciones')
def operaciones():
    if request.method == "GET":
        return render_template('opeaciones.html')
    
@app.route('/operaciones2')
def operaciones2():
    if request.method == "GET":
        return render_template('operaciones2.html')
    
@app.route('/resultado2',methods=['POST'])
def resultado2():
    numero1 = request.form.get('n1')
    numero2 = request.form.get('n2')
    count = 0
    resultado = 0
    res = ''
    while count < int(numero1):
        resultado += int(numero2)
        res += '{}+'.format(int(numero2))
        count += 1
    return render_template('resultado2.html',resultado = resultado,serie = res)

@app.route('/resultado2',methods=['POST'])
def resultado():
    numero1 = request.form.get('n1')
    numero2 = request.form.get('n2')
    resultado = int(numero1)*int(numero2)
    return render_template('resultado.html',n1= numero1,n2 = numero2,resultado = resultado)

@app.route('/tabla')
def tabla():
    return render_template('base.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/ruta2/<string:nom>')
def ruta2(nom):
    return "<h1>Ruta 2</h1>"+"<br>Hola {}".format(nom)

@app.route('/ruta3/<int:num>')
def ruta3(num):

    return "<h1>Ruta 3</h1>"+"<br>El numero es: {}".format(num)

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
    suma = n1+n2
    return "La suma de {} y {} es: {}".format(float(n1),float(n2),suma)



if __name__=="__main__":

    app.run(debug=True,port= 3000)