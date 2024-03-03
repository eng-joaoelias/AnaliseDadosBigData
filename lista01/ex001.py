def verPositivos(lista):
    listaNumerosPositivos = []
    for i in range(len(lista)):
        if lista[i] > 0:
            listaNumerosPositivos.append(lista[i])

    return listaNumerosPositivos

def main():

    listaNumeros = []
    
    tamLista = int(input("Entre com a quantidade de números para serem adicionados à lista>>"))

    for i in range(tamLista):
        valorASerAdd = int(input("Entre com o {} valor>> ".format(i+1)))
        listaNumeros.append(valorASerAdd)

    print("Números positivos informados >> {}".format(verPositivos(listaNumeros)))

if __name__ == "__main__":
    main()
