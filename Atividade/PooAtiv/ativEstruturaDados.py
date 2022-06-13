import math

#Numeros Complexos
class numerosComplex:
    def __init__ (self,a,b):
        self.a = a
        self.b = b

    def aComplex(self):
        numA = int(input("Digite o primeiro Numero "))
        numB = int(input('Digite o segundo numero '))
        self.a = complex(numA, numB)
        print(type(self.a))
        print(self.a)

teste = numerosComplex(1,1)
teste.aComplex()