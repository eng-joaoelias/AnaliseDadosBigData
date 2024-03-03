import datetime

def funcaoQ04(caminhoArquivo, palavra1, palavra2):
    # Lê o conteúdo do arquivo
    with open(caminhoArquivo, 'r') as arquivo:
        conteudo = arquivo.read()

    novoConteudo = conteudo.replace(palavra1, palavra2)

    numRepetPalavraAnterior = conteudo.count(palavra1)

    diaHoje = str(datetime.date.today().day)
    mesHoje = str(datetime.date.today().month)
    anoHoje = str(datetime.date.today().year)

    nome_novo_arquivo = palavra1 + "_" + palavra2 + "_" + diaHoje + "_" + mesHoje + "_" + anoHoje + "_" + str(numRepetPalavraAnterior) + ".txt"

    with open(nome_novo_arquivo, 'w') as novoArquivo:
        novoArquivo.write(novoConteudo)

    print(f"Arquivo modificado salvo como {nome_novo_arquivo}")

funcaoQ04("exemplo.txt", "antiga", "nova")
