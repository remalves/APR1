matriz = []
n=int(input("informe a qtd de linhas: "))
m=int(input("informe a qtd de colunas: "))

i=0#indice de linhas
while i < n:
    print(f"informe os elementos da linha {i}: ")

    linha=[]
    j=0 #indice de coluna 
    while j<m:
      elemento = int(input(f"Informe o valor da coluna {j}"))  
      linha.append(elemento)
      j+=1
    #insere o elemento na matriz
    matriz.append(linha)
    i+=1

    while i < len(matriz):
       j=0
       while j < len(matriz[i]):
          print(matriz[i][j], end = '')
          j+=1
       
       i+=1