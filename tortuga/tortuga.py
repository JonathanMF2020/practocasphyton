import turtle

def main():
    window = turtle.Screen()
    tortuga = turtle.Turtle()
    tortuga.shape('turtle')
    make_square(tortuga)
    turtle.mainloop()

def make_square(param):
    length = int(input('Tamaño de cuadrado: '))
    for i in range(4):
        crear_linea_gire(param,length)


def crear_linea_gire(param,longitud):
    param.forward(longitud)
    param.right(90)
    param.right(30)
        
    

if __name__ == "__main__":
    main()
    