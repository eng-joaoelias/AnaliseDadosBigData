def calculosEstatisticos(listaTemperaturas):
    listaTemperaturas.sort()

    acum = 0

    for temperatura in listaTemperaturas:
        acum = acum + temperatura
        
    media = acum / len(listaTemperaturas)

    mediana = 0

    print(f'O conjunto informado é {listaTemperaturas}')

    if len(listaTemperaturas) % 2 == 0:
        pos1 = int(len(listaTemperaturas) / 2 - 1)
        pos2 = pos1 + 1
        mediana = (listaTemperaturas[pos1] + listaTemperaturas[pos2]) / 2
    else:
        pos = int((len(listaTemperaturas) + 1) / 2 - 1)
        mediana = listaTemperaturas[pos]
        
    contagem = {}

    for elemento in listaTemperaturas:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
            
    moda = max(contagem, key=contagem.get)

    print(f'A média é {media}')
    print(f'A mediana é {mediana}')
    print(f'A moda é {moda}')

    numeradorVariancia = 0

    for elemento in listaTemperaturas:
        numeradorVariancia += (elemento - media) ** 2
    variancia = numeradorVariancia / len(listaTemperaturas)
    
    print(f'A variância é {variancia}')

    desvioPad = variancia ** (0.5)
    
    print(f'O desvio padrão é {desvioPad}')
    valoresEstatistica = []
    valoresEstatistica.append(media)
    valoresEstatistica.append(mediana)
    valoresEstatistica.append(moda)
    valoresEstatistica.append(variancia)
    valoresEstatistica.append(desvioPad)
    return valoresEstatistica
    
def main():
    
    listaTemperaturas = [19.5, 19.5, 21.6, 20.2, 19.7, 20.2, 18.6, 17.2, 19.5]

    lista1 = calculosEstatisticos(listaTemperaturas)
    listaTemperaturas.append(20.2)
    lista2 = calculosEstatisticos(listaTemperaturas)
    
    if lista1[0] < lista2[0]:
        print('A média aumentou!')
    else:
        print('Diminuição da média')
        
    if lista1[1] < lista2[1]:
        print('A mediana aumentou!')
    else:
        print('Diminuição da mediana')
        
    if lista1[2] < lista2[2]:
        print('A moda aumentou!')
    else:
        print('Diminuição da moda')
        
    if lista1[3] < lista2[3]:
        print('A variância aumentou!')
    else:
        print('Diminuição da variância')
        
    if lista1[4] < lista2[4]:
        print('O desvio padrão aumentou!')
    else:
        print('Diminuição do desvio padrão')
    
if __name__ == "__main__":
    main()
