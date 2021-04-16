
class Calculo:
    arreglo1 = []
    arreglo2 = []
    
    def __init__(self, areglo,areglo2):
        self.arreglo1 = areglo
        self.arreglo2 = areglo2
        
    def operacion(self):
        print(arreglo1[1][0])
        resultado1 = (((-1)**(1+1)))*arreglo1[1][1]
        resultado2 = (((-1)**(1+2)))*arreglo1[1][0]
        resultado3 = (((-1)**(2+1)))*arreglo1[0][1]
        resultado4 = (((-1)**(2+2)))*arreglo1[0][0]
        print(str(resultado1)+' ' +str(resultado3)+' '+str(resultado2)+' ' +str(resultado4))
        adjuntos=[[resultado1,resultado3],[resultado2,resultado4]]
        res1=(adjuntos[0][0]*arreglo2[0][0])+(adjuntos[0][1]*arreglo2[1][0])
        res2=(adjuntos[0][0]*arreglo2[0][1])+(adjuntos[0][1]*arreglo2[1][1])
        res3=(adjuntos[1][0]*arreglo2[0][0])+(adjuntos[1][1]*arreglo2[1][0])
        res4=(adjuntos[1][0]*arreglo2[0][1])+(adjuntos[1][1]*arreglo2[1][1])
        print(str(res1)+' ' +str(res2)+' '+str(res3)+' ' +str(res4))


if __name__ == "__main__":
    arreglo1 = [[3,-1],[1,0]]
    arreglo2 = [[4,2],[-1,3]]
    objeto = Calculo(arreglo1,arreglo2)
    objeto.operacion()

