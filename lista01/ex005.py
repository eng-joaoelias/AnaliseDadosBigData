def pedirNome():
    nome = input("Digite o seu nome>> ")
    if len(nome) > 3:
        return 0
    else:
        print("Valor inválido.")
        return 1
    
def pedirIdade():
    idade = int(input("Digite sua idade>> "))
    if idade >= 0 and idade <= 150:
        return 0
    else:
        print("Valor inválido.")
        return 1

def pedirSalario():
    salario = float(input("Digite o seu salário>> R$"))
    if salario > 0:
        return 0
    else:
        print("Valor inválido.")
        return 1
    
def pedirSexo():
    sexo = input("Digite o seu sexo biológico (M/F)>>")
    if sexo == 'F' or sexo =='M' or sexo == 'f' or sexo == 'm':
        return 0
    else:
        print("Valor inválido.")
        return 1
    
def pedirEstadoCivil():
    print("Informe aqui seu estado civil.\nOpções:\nS - Solteiro\nC - Casado(a)\nV - Viúvo(a)\nD - Divorciado(a)")
    estCivil = input("Escolha: ")
    if estCivil.upper() == 'S' or estCivil.upper() == 'C' or estCivil.upper() == 'V' or estCivil.upper() == 'D':
        return 0
    else:
        print("Valor inválido.")
        return 1
    
def main():
    retornoNome = pedirNome()
    while(retornoNome == 1):
        retornoNome = pedirNome()

    retornoIdade = pedirIdade()
    while(retornoIdade == 1):
        retornoIdade = pedirIdade()

    retornoSalario = pedirSalario()
    while(retornoSalario == 1):
        retornoSalario = pedirSalario()

    retornoSexo = pedirSexo()
    while(retornoSexo == 1):
        retornoSexo = pedirSexo()

    retornoEstCivil = pedirEstadoCivil()
    while(retornoEstCivil == 1):
        retornoEstCivil = pedirEstadoCivil()


if __name__ == "__main__":
    main()
