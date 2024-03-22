def geraMatriz(char_init, char_final, num_init, num_final):
    
    matriz = []
    
    for i in range(num_init, num_final + 1):
        
        linha = []
        
        for j in range(ord(char_init), ord(char_final) + 1):
            linha.append(chr(j) + str(i))
        
        matriz.append(linha)
        
    return matriz
            
def main():
    matriz = geraMatriz('A', 'D', 1, 5)
    for linha in matriz:
        print(" ".join(linha))
    
if __name__ == "__main__":
    main()
