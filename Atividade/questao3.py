inicio = int(input("inicio: "))
fim = int(input("fim: "))
verificador = int(input("verificador: "))
if verificador < inicio or verificador > fim :
    if verificador < inicio:
        print (verificador,'é menor que', inicio)
    elif (verificador > fim):
        print(verificador,' é maior que', fim)
else:
    print(verificador,'está dentro de ', inicio,' e', fim)