'''Crie um programa que solicita do usuário um valor N representando a
quantidade linhas e um valor M representando a quantidade de colunas
de uma matriz. Depois, o programa deverá solicitar do usuário N x M
elementos para serem incluídos na matriz. Por fim, o programa deverá
percorrer a matriz para encontrar e imprimir o seu maior elemento e o
seu menor elemento.
'''

matriz = []

n=int(input("Digite quantas linhas a matriz tera: "))
m=int(input("Digite quantas colunas a matriz tera: "))

i=0
while i<n:
    print(f"informe os elementos da linha {i}: ")
    print()
    linha = []
    j=0 #indice de coluna 
    while j < m: 
        elemento = int(input(f"Informe o valor da coluna {j}: "))
        print()
        linha.append(elemento)
        j+=1 
    #inserindo o elemento na matriz 
    matriz.append(linha)
    i+=1

i=0
maior = matriz[0][0]
menor = matriz[0][0]
while i < len(matriz):
   j=0
   while j < len(matriz[i]): 
       if matriz[i][j] > maior:
           maior = matriz[i][j]
           if matriz[i][j] < menor:
               menor = matriz[i][j] 
       j+=1
   i+=1


print(f"maior valor: {maior}")
print(f"menor valor: {menor}")




    


