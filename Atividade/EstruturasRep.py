# Fatorial
fatorial = int(input('Digite um fatorial: '))
contador = fatorial
fator = 1

indice = 2

while indice <= fatorial:
    contador -= 1
    fator= fator*indice
    indice += 1
    estiloContador = contador
    print(f'{fatorial}!{estiloContador} * {estiloContador} = {fator}',end='')

