def cambiomoneda(cantidad):
    dolar = 20.0
    return cantidad/dolar

def main():
    print('C A M B I O')
    print('Convierte pesos a dolares')
    cantidad = float(input('Ingresa la cantidad de pesos que se quiere convertir'))
    resultado = cambiomoneda(cantidad)
    print('Tienes {} y son {} dolares'.format(cantidad,resultado))

if __name__ == "__main__":
    main()