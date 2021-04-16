import os
import math

class circulo:
    radio = 0
    
    def __init__ (self,radioo):
        self.radio = radioo
        
    def area(self):
        return (self.radio**2)*math.pi
    
class cuadrado:
    l1 = 0
    
    def __init__ (self,l1):
        self.l1 = l1
        
    def area(self):
        return self.l1*self.l1
    
    
class triangulo:
    base = 0
    altura = 0
    
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return (self.base*self.altura)/2

if __name__ == "__main__":
    id = 1
    while id >= 1 :
        print("Areas de figuras")
        print("1.- Area circulo")
        print("2.- Area cuadrado")
        print("3.- Area triangulo")
        print("0 .- Salir")
        id = int(input("Ingresa la opcion a la que decides ir: "))
        os.system ("cls") 
        if id == 1:
            r = float(input("Ingresa el radio: "))
            circ = circulo(r)
            print("----------------------------------------------------")
            print("El radio del circulo es: {}".format(circ.area()))
            print("----------------------------------------------------")
        if id == 2:
            l1 = float(input("Ingresa el lado: "))
            cuad = cuadrado(l1)
            print("----------------------------------------------------")
            print("El radio del cuadrado es: {}".format(cuad.area()))
            print("----------------------------------------------------")
        if id == 3:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            tri = triangulo(base,altura)
            print("----------------------------------------------------")
            print("El radio del triangulo es: {}".format(tri.area()))
            print("----------------------------------------------------")            
            

    


    