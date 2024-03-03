# Solicita ao usuário que digite uma frase e armazena a entrada na variável "frase"
frase = input("Vamos lá! Digite alguma frase aqui>> ")

# Divide a frase em palavras e armazena as palavras em uma lista chamada "vetorPalavras"
vetorPalavras = frase.split()

# Cria um dicionário vazio chamado "contagemPalavras" para armazenar as contagens de cada palavra
contagemPalavras = {}

# Itera sobre cada palavra na lista "vetorPalavras"
for palavra in vetorPalavras:
    # Verifica se a palavra já está no dicionário "contagemPalavras"
    if palavra in contagemPalavras:
        # Se a palavra já estiver no dicionário, incrementa sua contagem em 1
        contagemPalavras[palavra] += 1
    else:
        # Se a palavra não estiver no dicionário, adiciona-a ao dicionário com uma contagem inicial de 1
        contagemPalavras[palavra] = 1

# Imprime o dicionário "contagemPalavras" contendo as contagens de cada palavra na frase
print(contagemPalavras)
