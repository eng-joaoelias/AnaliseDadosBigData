qtdTermos = int(input("Entre com a quantidade de termos de Fibonacci>>"))
vctTermos = [0, 1]
for cont in range(2, qtdTermos - 2):
    vctTermos.append(vctTermos[cont-1] + vctTermos[cont-2])
print("Termos>> {}".format(vctTermos))
