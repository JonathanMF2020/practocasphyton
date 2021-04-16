if __name__ == "__main__":
    n1 = int(input('Ingresa el numero 1: '))
    n2 = int(input('Ingresa el numero 2: '))
    for x in range(n1+1, n2-1):
        if x % 2 == 0:
            print(x)