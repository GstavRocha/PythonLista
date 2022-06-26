#https://www.w3schools.com/python/ref_math_cos.asp
#https://www.arquivodecodigos.com.br/dicas/4032-python-como-calcular-o-seno-de-um-numero-ou-angulo-em-python-usando-a-funcao-sin-do-modulo-math.html

import math
import cmath

#Numeros Complexos
class CoordCartesians:
    def __init__(self):
        a = int(input(" Digite A "))
        b = int(input(" Digite B "))
        self.a = a.real
        self.b = b .imag
        n = complex(a,b)
        print(n)

class Polares:
    def __init__(self):
        self.r = int(input(" defina R "))
        self.alfa = int(input( " defina Alfa "))
    
    def cos(self):
         return math.cos(self.alfa)
    def sin(self):
        return math.sin(self.alfa)
    
    def resultado(self):
       n = self.r * self.cos + self.r * self.sin
       return n


teste1 = CoordCartesians()
teste2 = Polares()
# Não funcionou!
