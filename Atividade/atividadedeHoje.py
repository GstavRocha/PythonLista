# ponto inicial
ponto1 = int(input('Digite o primeiro numero: '))
ponto2 = int(input('Digite o segundo numero: '))
ponto3 = int(input('Digite o terceiro numero: '))
ponto4 = int(input('Digite o quarto numero: '))

pontoA = 'A'
pontoB = 'B'
pontoC = 'C'
pontoD = 'D'
pontoE = 'E'
pontoF = 'F'
pontoG = 'G'

medidor = 0
print(pontoA,end=' -> ')
medidor= ponto1 + ponto2
if(ponto1 < ponto2):
    print( pontoB,end=' -> ' )
    if(ponto3 < ponto4):
        print(pontoD)
        medidor = ponto1 + ponto3
    else:
        print(pontoE)
        medidor = ponto1 + ponto4
else:
    print( pontoC,end=' -> ')
    if(ponto3 < ponto4):
        print(pontoF)
        medidor = ponto2 + ponto3
    else:
        print(pontoG)
        medidor = ponto2 + ponto4
print(medidor)