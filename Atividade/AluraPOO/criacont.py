def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

conta = cria_conta(123,'Gustavo',500,1000)

print(conta('titular'))
