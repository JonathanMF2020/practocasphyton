import string
def rango(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


def completar(lastValue):
    while len(lastValue) < 5:
        lastValue += 'X'
    return lastValue


def convertir(letras):
    lista = []
    for letra in letras:
        lista.append(int(ord(letra) % 32))

    return lista


if __name__ == "__main__":
    ingreso = input('Inserta la primera frase: ')
    ingreso2 = input('Inserta una segunda frase de la misma longitud: ')
    ingreso = ingreso.replace(" ", "").upper()
    ingreso2 = ingreso2.replace(" ", "").upper()
    newingreso = list(rango(ingreso, 5))
    newingreso2 = list(rango(ingreso2, 5))
    valor = newingreso[len(newingreso)-1]
    valor = completar(valor)
    newingreso[len(newingreso)-1] = valor
    valor = newingreso2[len(newingreso2)-1]
    valor = completar(valor)
    newingreso2[len(newingreso2)-1] = valor
    lista1 = convertir(ingreso)
    lista2 = convertir(ingreso2)
    print(f'List1: {lista1} Lista2: {lista2}')
    print(f'Cadena1: {ingreso} Cadena2:{ingreso2}')
    listanueva = []
    for x in range(len(lista1)):
        r = int(lista1[x]) + int(lista2[x])
        if r > 26:
            r -= 26
        listanueva.append(r)
    cifrado = ""
    for l in listanueva:
        cifrado += str(chr(ord('@')+l))

    print([cifrado[i:i+5] for i in range(0,len(cifrado),5)])
        
    
        
            
