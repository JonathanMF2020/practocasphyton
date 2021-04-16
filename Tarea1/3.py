
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
    lista = []
    repetir_bucle = True
    while repetir_bucle:
        valor = int(input("Ingresa un valor para meter a la lista (-1 para salir): "))
        if valor == -1:
            break
        lista.append(valor)  
    print("Vamos a buscar en la siguiente lista:", lista)
    busqueda = int(input("Cual numero quieres buscar: "))
    indice = busqueda_binaria_recursiva(lista, busqueda, 0, len(lista) - 1)
    if(indice == -1):
        print("El numero no se encuentra dentro de la lista")
    else:
        print('Posicion {}'.format(indice))
        