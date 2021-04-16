




if __name__ == "__main__":
    archivo = open("tarea23/mbox-short.txt","r")
    listar = archivo.readlines()
    for item in listar:
        print(item.upper())
    
    