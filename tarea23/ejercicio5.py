class calculo():
    sum = 0
    n = 0
    def __init__(self, n):
        self.n = 0
        
    def getCalculo(self):
        for i in range(0, n):
            self.sum += 1/(2**i)
        return self.sum


if __name__ == "__main__":
    n = int(input('Ingrese un número: '))
    print("El resultado {}".format(calculo(n).getCalculo()))