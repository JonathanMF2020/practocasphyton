class Boletos:
    boletos = 0
    total = 0
    
    def __init__ (self,boletoss):
        self.boletos = boletoss
        self.total = 0
        
    def comprar(self):
        if(self.boletos > 7):
            self.total = -1
            return self.total
        self.total = self.boletos*12000
        if self.boletos > 5:
            self.total = self.total - (self.total*0.15)
        if self.boletos == 3:
            self.total = self.total - (self.total*0.10)
        if self.boletos == 4:
            self.total = self.total - (self.total*0.10)
        if self.boletos == 5:
            self.total = self.total - (self.total*0.10)
        return self.total
    
    def tarjeta(self):
        self.total = self.total - (self.total*0.10)
            
            


if __name__ == "__main__":
    b = int(input("Ingresa la cantidad de boletos comprados: "))
    circ = Boletos(b)
    circ.comprar()
    final = float(format(circ.total))
    if(final == -1):
        print("Solo puedes comprar hasta 7 boletos por persona")
    else:
        print("Total a pagar: {}".format(final))
        tarjeta =  int(input("¿Tienes alguna tarjeta CINECO?\n1.- Si\n2.- No\n:"))
        if tarjeta == 1:
            circ.tarjeta()
            final2 = float(format(circ.total))
            print("Total neto a pagar con tarjeta {}".format(final2))
        else:
            print("Total neto a pagar {}".format(final))
    