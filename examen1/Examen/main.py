from flask import Flask, render_template
from flask import request
from cesar import *
from calculo import *
from io import open

app=Flask(__name__)



    
@app.route('/cifrar',methods=['GET','POST'])
def index():
    if request.method == "POST":
        palabra = request.form.get("palabra")
        codigo = request.form.get("codigo")
        obj = cesar(palabra,codigo)
        resultado = obj.cifrar()
        rep = '{},{},{}\n'.format(str(palabra),str(codigo),str(resultado))
        archivo_text = open('archivo.txt', 'w', encoding='utf-8')
        archivo_text.write(rep)
        archivo_text.close()
        return render_template("index.html",resultado=resultado)
    else: 
        return render_template("index.html")
    
@app.route('/',methods=['GET','POST'])
def index2():
        return render_template("index.html")
    
@app.route('/descifrar',methods=['GET','POST'])
def descifrar():
    if request.method == "POST":
        palabra = request.form.get("palabra")
        codigo = request.form.get("codigo")
        obj = cesar(palabra,codigo)
        resultado = obj.descifrar()
        return render_template("index2.html",resultado=resultado)
    else: 
        return render_template("index2.html")
    
@app.route('/ejercicio2',methods=['GET','POST'])
def ejercicio2():
    if request.method == "POST":
        m1v1 = request.form.get("m1v1")
        m1v2 = request.form.get("m1v2")
        m1v3 = request.form.get("m1v3")
        m1v4 = request.form.get("m1v4")
        m2v1 = request.form.get("m2v1")
        m2v2 = request.form.get("m2v2")
        m2v3 = request.form.get("m2v3")
        m2v4 = request.form.get("m2v4")
        arreglo1 = []
        arreglo2 = []
        arreglo1.append(int(m1v1))
        arreglo1.append(int(m1v2))
        arreglo1.append(int(m1v3))
        arreglo1.append(int(m1v4))
        arreglo2.append(int(m2v1))
        arreglo2.append(int(m2v2))
        arreglo2.append(int(m2v3))
        arreglo2.append(int(m2v4))      
        obj = calculo(arreglo1,arreglo2)
        resultado = obj.operacion()
        return render_template("ejercicio2.html",resultado=resultado)
    else: 
        return render_template("ejercicio2.html")
        
    
    
    
if __name__=="__main__":

    app.run(debug=True,port= 3000)