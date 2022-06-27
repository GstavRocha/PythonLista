# Atividade de Listas
lista = [1,2,3,4,5,6,7]
print(lista[::-1])
print(lista[1::-1])
print(lista[:-3:-1])

for i in range(len(lista)):
    print(lista[:-7], end=',')

nota1  = [1,2,3,4,5,6,7,8,9]
print(nota1)
nota2 = nota1 
nota1[0]= 18 # muda tanto para nota1 quanto para nota2.
print(nota2)
nota2[2] = 13
print(nota1) # muda 

# Resolvendo o problema de referência de lista.

lista1 = [1,2,3,4,5,6,7,8]
lista2 = []
for i in lista1:
    lista2 +=[i]
    print(lista2)

listaA = [1,2,3,4,5,6,7,8,9]
listaB = listaA[:] # slice não afeta listas.
listaB[0] = 33
listaA[3] = 13
print (listaA)
print(listaB)