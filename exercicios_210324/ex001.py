listaTmeperaturas = [19.5, 19.5, 21.6, 20.2, 19.7, 20.2, 18.6, 17.2, 19.5]

def calculosEstatisticos():
    listaTmeperaturas.sort()

    acum = 0

    for temperatura in listaTmeperaturas:
        acum = acum + temperatura
        
    media = acum / len(listaTmeperaturas)

    mediana = 0

    print(f'O conjunto informado é {listaTmeperaturas}')

    if len(listaTmeperaturas) % 2 == 0:
        pos1 = int(len(listaTmeperaturas) / (2) - 1)
        pos2 = pos1 + 1
        mediana = (listaTmeperaturas[pos1] + listaTmeperaturas[pos2]) / 2
    else:
        pos = int((len(listaTmeperaturas) + 1) / (2) - 1)
        mediana = listaTmeperaturas[pos]
        
    contagem = {}

    for elemento in listaTmeperaturas:
        if elemento in contagem:
            contagem[elemento] = contagem[elemento] + 1
        else:
            contagem[elemento] = 1
            
    moda = max(contagem, key = contagem.get)

    print(f'A média é {media}')
    print(f'A mediana é {mediana}')
    print(f'A moda é {moda}')

    numeradorVariancia = 0

    for elemento in listaTmeperaturas:
        numeradorVariancia = numeradorVariancia + ((elemento - media)**2)
    variancia = numeradorVariancia / len(listaTmeperaturas)
    
    print(f'A variância é {variancia}')

    desvioPad = variancia ** (0.5)
    
    print(f'O desvio padrão é {desvioPad}')
    
calculosEstatisticos()
listaTmeperaturas.append(20.2)
calculosEstatisticos()
