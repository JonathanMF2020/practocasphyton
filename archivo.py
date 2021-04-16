from io import open

archivo = open("archivo.txt","w")
i = 1
cadena = ""
while i <= 100:
    i = i+1
    cadena += "{}\n".format(int(i))
    print(cadena)
    
archivo.write(cadena)
archivo.close()