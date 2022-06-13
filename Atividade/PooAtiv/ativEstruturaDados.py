from distutils.command.clean import clean
import math

#Numeros Complexos
class numerosComplex:
    def __init__ (self,a,b):
        self.a = a
        self.b = b
class Cartesianas(numerosComplex):
    def __init__(self,a):
        super().__init__(self,a)

    def complexSimples (self):
        numA = int(input('Primeiro Numero '))
        numB = int(input('Segundo Numero '))
        self.a = complex(numA,numB)
        print(self.a)

class Polares(numerosComplex):
    def __init__(self,b):
        super().__init__(self,b)
    def cosen(self):
        https://www.w3schools.com/python/ref_math_cos.asp

teste = numerosAcomp(1)
teste.complexSimples()

    