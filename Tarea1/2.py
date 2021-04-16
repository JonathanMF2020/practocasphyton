
def Calcular(precio1,precio2,precio3):
    r = (precio1+precio2+precio3)/3
    return r

if __name__ == "__main__":
    p1 = float(input("Introduce el precio del producto en el establecimiento numero 1 en euros: "))
    p2 = float(input("Introduce el precio del producto en el establecimiento numero 2 en euros: "))
    p3 = float(input("Introduce el precio del producto en el establecimiento numero 3 en euros: "))
    resultado = Calcular(p1,p2,p3)
    print("El precio medio del producto es: {}".format(resultado))

