#https://blogengenharia.universidadedevassouras.edu.br/publicacoes/estrutura-de-dados-em-python-trabalhando-com-listas/#:~:text=As%20listas%20s%C3%A3o%20estruturas%20lineares,da%20posi%C3%A7%C3%A3o%203%20%C3%A9%20cer%C3%A2mica.

nomes = ['gustavo', 'dany', 'deborah', 'lucky', 'cocada']

# print(nomes[1]) 
# print(len(nomes))

nomes.append('zeca')
nomes.append('toli')
nomes.append('zara')
nomes.append('deinha')
nomes.append('neta')
nomes.append('jojo')
nomes.append('jacare')
nomes.append('pedim')
# print(nomes)

# print(len(nomes))

def busca(lista, elemento): #função para procurar
    lista = nomes
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None

nomes
elemento =str(input(" procure o nome "))

procurar = busca(nomes,elemento)
if procurar is not None:
    print("O elemento encontrado {} é o {}".format(elemento, procurar))
else:
    print("Elementos não encontrados na lista {} nesse caso ele foi adicionado".format(nomes))
    nomes.append(elemento)
    print(nomes)
print("nomes fora {}".format(nomes))