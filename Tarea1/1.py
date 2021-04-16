import math


def CalcularVolumen(diametro,altura):
    r = diametro/2
    v = math.pi*(r**3)*altura
    return v

if __name__ == "__main__":
    d = float(input("Introduzca el diametro en metros"))
    h = float(input("Introduzca la altura en metros"))
    resultado = CalcularVolumen(d,h)
    print("El volumen del cilindro es de {} metros cubicos".format(resultado))