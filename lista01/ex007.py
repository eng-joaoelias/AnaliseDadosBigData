def fibonacci(qtdTermos):
    if qtdTermos == 1:
        return [1]
    elif qtdTermos == 2:
        return [1, 1]
    else:
        seq = fibonacci(qtdTermos - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

qtdTermos = 5
resultado = fibonacci(qtdTermos)
print("Sequência de Fibonacci até o {}º termo:".format(qtdTermos))
print(resultado)
