temperatura = int(input('Digite a temperatura: '))
while( temperatura >= 0):
    if(temperatura <=  15):
        print(' Aqui não é o RN')
    elif(temperatura >= 16 and temperatura <= 25):
        print('Temperatura normal e super agradavel')
    elif(temperatura >= 31 and temperatura <= 35):
        print('Tá quente pra danado')
    elif(temperatura > 35):
        print('Calor da múlestia')
    temperatura = int(input('Digite a temperatura: '))