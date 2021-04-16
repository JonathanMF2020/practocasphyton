if __name__ == "__main__":
    concatNombre(capturarNombre())
    
    
def saludo():
    print("Hola esto es un saludo")
    
def capturarNombre():
    nombre = input("Give your name")
    return nombre

def concatNombre(nom):
    print("Hola {} {}".format(nom,"Hola"))
    saludo()
    
