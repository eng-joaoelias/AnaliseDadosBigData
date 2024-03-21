def fibonacci(qtdTermos):
    x = 0
    if qtdTermos == 1:
        x = 1
        return x
    if qtdTermos == 2:
        x = 1
        return x
    x = fibonacci(qtdTermos - 1) + fibonacci(qtdTermos - 2)
    print(x)
    return x
    
print(fibonacci(8))
