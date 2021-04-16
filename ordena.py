from io import open


def busqueda_binaria_recursiva(arreglo, busqueda, izquierda, derecha):
    if izquierda > derecha:
        return -1
    indiceDelElementoDelMedio = (izquierda + derecha) // 2
    elementoDelMedio = arreglo[indiceDelElementoDelMedio]
    if elementoDelMedio == busqueda:
        return indiceDelElementoDelMedio
    if busqueda < elementoDelMedio:
        return busqueda_binaria_recursiva(arreglo, busqueda, izquierda, indiceDelElementoDelMedio - 1)
    else:
        return busqueda_binaria_recursiva(arreglo, busqueda, indiceDelElementoDelMedio + 1, derecha)
    
if __name__ == "__main__":
    
    print("Hola")
    archivo = open("archivo.txt","r")
    listar = archivo.readlines()
    lista = [int(item) for item in listar]
    print("Vamos a buscar en la siguiente lista:", lista)
    busqueda = int(input("Cual numero quieres buscar: "))
    indice = busqueda_binaria_recursiva(lista, busqueda, 0, len(lista) - 1)
    if(indice == -1):
        print("El numero no se encuentra dentro de la lista")
    else:
        print('Posicion {}'.format(indice))
        