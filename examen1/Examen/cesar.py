class cesar():
    texto = ''
    key = ''
    value = 0

    def __init__(self, texto, value):
        self.texto = texto.upper()
        self.value = value

    def cifrar(self):

        map(int, str(self.value))

        i = 0
        for letra in self.texto:
            if letra == ' ':
                self.key += letra
                i += 1
                if i > (len(self.value)-1):
                    i = 0
            else:
                x = int(ord(letra) % 32)

                x += int(self.value[i])
                if x > 26:
                    x -= 26
                self.key += chr(ord('@')+x)
            i += 1
            if i > (len(self.value)-1):
                i = 0
        return self.key
    

    def descifrar(self):

        map(int, str(self.value))

        i = 0
        for letra in self.texto:
            if letra == ' ':
                self.key += letra
                i += 1
                if i > (len(self.value)-1):
                    i = 0
            else:
                x = int(ord(letra) % 32)

                x -= int(self.value[i])
                if x < 1:
                    x += 26
                self.key += chr(ord('@')+x)
            i += 1
            if i > (len(self.value)-1):
                i = 0
        return self.key