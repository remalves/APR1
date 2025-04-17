matriz = []
li = 3
coluna = 2 

i=0
while i < li: 
    linha = []
    print(f"Digite os elementos da linha {i}: ")
    print()
    j=0
    while j < coluna:
        
        valor = int(input(f"Digite um elemento para a coluna {j}: "))
        print()
        linha.append(valor)
        j+=1
    matriz.append(linha)
    i+=1

transposta=[]
j=0
while j<len(matriz[j]): # número de colunas da matriz original (2)
    linha2=[]
    i=0
    while i<len(matriz): # número de linhas da matriz original (3)
        elemento = matriz[i][j]
        linha2.append(elemento)
        i+=1      
    transposta.append(linha2)
    j+=1


print("Matriz")
i=0
while i < len(matriz): 
    j=0
    while j<len(matriz[i]):
        print(matriz[i][j], end=' ')
        j+=1
    print()
    i+=1

print()
print("Matriz Transposta")
i = 0
while i < len(transposta): 
    j = 0
    while j < len(transposta[i]):
        print(transposta[i][j], end=' ')
        j += 1
    print()  # quebra a linha depois de imprimir uma linha completa
    i += 1