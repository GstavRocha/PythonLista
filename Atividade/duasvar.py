v_ini = int(input(' Digite o numero inicial '))
v_fim = int(input('Digite o numero final '))

if v_ini < v_fim:
    for i in range(v_ini+1,v_fim):
        print('{} '.format(i),end='') 
else:
    for i in range(v_ini-1, v_fim, -1):
        print('{} '.format(i),end='') 