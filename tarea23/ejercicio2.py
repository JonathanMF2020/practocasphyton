if __name__ == "__main__":
    lectura = input('Ingresa el nombre del archivo: ')
    cadena = "tarea23/"+lectura+".txt"
    archivo = open(cadena,"r")
    listar = archivo.readlines()
    valor = 0
    coincidencia = 0
    for item in listar:
        if item.startswith('X-DSPAM-Confidence'):
            print(item[19:26])
            suma = float(item[19:26])
            valor += suma
            coincidencia += 1
    print("Total de coincidencias: {}".format(coincidencia))
    print("Total resultado: {}".format(valor))
    resu = valor/coincidencia
    print("Promedio: {}".format(resu))
            
            
    
