
primo = int(input(" escolha um numero "))
divisiveis = 0
# por decomposição
if primo >= 1 and primo <= 10000:
    for i in range (1,primo +1):
        if primo % i == 0:
            print('\033[031m',end='')
            divisiveis += 1
        else:
            print('\033[34m',end='')
        print('{} '.format(i),end='') 
    print('\n\33[m O número {} foi dividido {} vezes'.format(primo,divisiveis))
    if divisiveis == 2:
        print('\n\33[m O número {} é primo'.format(primo))
    else:
        print('\n\33[m O numero {} não é primo'.format(primo))
else:
    print('\033[31m Você deve informar um número entre 1 e 10000')
