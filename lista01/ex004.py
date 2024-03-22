from datetime import date

def substituirPalavras(arquivo, palavraAnterior, palavraNova):
    with open(arquivo, 'r', encoding='utf-8') as arquivo:
        conteudoTexto = arquivo.read()

    contagemPalavraAterior = conteudoTexto.count(palavraAnterior)
        
    if palavraAnterior in conteudoTexto:
        conteudoTexto = conteudoTexto.replace(palavraAnterior, palavraNova)
    
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    
    nomeNovoArquivo = f"{palavraAnterior}_{palavraNova}_{dia}_{mes}_{ano}_{contagemPalavraAterior}.txt"
    
    with open(nomeNovoArquivo, 'w') as novoArquivo:
        novoArquivo.write(conteudoTexto)
        
def main():
    substituirPalavras('2024.1_lista_analise_de_dados_Q3.txt', 'paralelepípedo', 'vibrador')
    
if __name__ == "__main__":
    main()
