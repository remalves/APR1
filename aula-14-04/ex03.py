'''Faça um programa que solicite do usuário um valor N, representando
a dimensão de uma matriz quadrada (matriz A). Em seguida, o
programa deverá solicitar do usuário os elementos da matriz A e,
posteriormente, deverá verificar se A é simétrica. Obs: Matriz
simétrica: matriz quadrada de ordem n tal que A = A'''

n = int(input("Digite um valor: ")) 

matrizA = []

i=0
while i<n:
    print(f"informe os elementos da linha {i}: ")
    print()
    linha = []
    j=0 #indice coluna 
    while j < n:
        elemento = int(input(f"Informe o valor da coluna {j}: "))
        print()
        linha.append(elemento)
        j+=1
    matrizA.append(linha)
    i+=1

i=0
simetrica=0
while i < len(matrizA): 
    j=0
    while j<len(matrizA[i]):
        if matrizA[i][j] == matrizA[j][i]:
            simetrica=1
        j+=1
    i+=1

        
if simetrica == 1: 
    print("simetrica")
else:
    print("nao simetrica") 




# matrizT=[]
# j=0
# while j < len(matrizA[0]):#colunas (quantidade de colunas da linha 0)
#     linha2=[]
#     i=0
#     while i < len(matrizA):#linhas
#         linha2.append(matrizA[j][i]) #fixando o j, variamos a parte mais interna o i 
#         i+=1 
#     matrizT.append(linha2)
#     i+=1

           
           

