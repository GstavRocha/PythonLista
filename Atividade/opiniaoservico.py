from re import U


usuario = int(input(' quantas pessoas pesquisadas? '))
satisfeito = 0
insatisfeito = 0
naoResponder = 0
print('Pesquisa de opinião do nosso serviço')
while(usuario > 0):
    opiniao = int(input('satisfeito = 1, insatisfeito = 2, não quero responder = 3 \n'))
    if(opiniao == 1): 
        satisfeito +=1
    elif(opiniao == 2):
        insatisfeito +=1
    elif(opiniao == 3):
        naoResponder += 1
    usuario -=1

total = satisfeito + insatisfeito + naoResponder
satisPcent = (satisfeito * 100) / total
insatPcent = (insatisfeito*100) / total
naoResPcent = (naoResponder * 100) / total
print(f'Clientes satisfeito: {satisPcent}, Clientes insatisfeitos: {insatPcent}, Clientes que não responderam: {naoResPcent} total= {total}')
