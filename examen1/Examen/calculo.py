class calculo:
    arreglo1 = []
    arreglo2 = []
    
    def __init__(self, areglo,areglo2):
        self.arreglo1 = areglo
        self.arreglo2 = areglo2
        
    def operacion(self):
        arreglo11=[]
        matrizD=0
        n1=0
        n2=0
        matriz1=[]
        arreglo11.append(self.arreglo1[3])
        arreglo11.append(self.arreglo1[1]*(-1))
        arreglo11.append(self.arreglo1[2]*(-1))
        arreglo11.append(self.arreglo1[0])
        n1=(self.arreglo1[0]*self.arreglo1[3])
        n2=(self.arreglo1[1]*self.arreglo1[2])
        matrizD=n1-n2
        matriz1.append(arreglo11[0]/matrizD)
        matriz1.append(arreglo11[1]/matrizD)
        matriz1.append(arreglo11[2]/matrizD)
        matriz1.append(arreglo11[3]/matrizD)
        matrizRespuesta=[]
        matrizRespuesta.append((matriz1[0]*self.arreglo2[0])+(matriz1[1]*self.arreglo2[2]))
        matrizRespuesta.append((matriz1[0]*self.arreglo2[1])+(matriz1[1]*self.arreglo2[3]))
        matrizRespuesta.append((matriz1[2]*self.arreglo2[0])+(matriz1[3]*self.arreglo2[2]))
        matrizRespuesta.append((matriz1[2]*self.arreglo2[1])+(matriz1[3]*self.arreglo2[3]))
        return matrizRespuesta