def fibonacci(qtdTermos):
    if qtdTermos == 1:
        return 1
    if qtdTermos == 2:
        return 1
    x = fibonacci(qtdTermos - 1) + fibonacci(qtdTermos - 2)
    print(x)
    return x
    
print(fibonacci(8))
