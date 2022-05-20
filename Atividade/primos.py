#https://www.somatematica.com.br/fundam/primos.php#:~:text=Para%20saber%20se%20um%20n%C3%BAmero,caso%20o%20n%C3%BAmero%20%C3%A9%20primo.
primos = int(input(" escolha um numero "))
num = 10000
# por decomposição
for i in range (primos,num):
    if primos % i == 0:
        print('não é primo')
    elif primos % 5 == 0 or primos% 5 == 5:
        print( 'teste')

