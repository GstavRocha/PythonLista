# Material do professor analise de Lista:
lista = [1, 8, 4, 9, 5]
print(lista)
#ALterando indice 3 de 9 para 7

lista[3] = 7
print(lista)

#pecorrendo a lista:
for indice in lista:
    print(indice, end=',')
    print('\n')
#pecorrendo a lista e imprimindo os itens pelo indice

for i in range(len(lista)): # função len retorna tamanho da lista
    print(lista[i], end=',')

#https://drive.google.com/file/d/14pZNJ_1lP3Ut_oxLyePWwFZm4-AIhDjs/view
# não entendi como é a questão das referências de memória