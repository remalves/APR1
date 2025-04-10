
N = int(input("Informe a quantidade de elementos: "))

L =[]
i=0
while i < N:
    num =int(input("entre com a nota: "))
    L.append(num)
    i+=1

soma = 0 #guarda a somatoria dos elementos pares
produto = 1 #guarda a produtorio dos elementos impares
i=0
while i<len(L):
    #verifica se é par
    if L[i]%2==0:
        soma+=L[i]
    else: 
        produto *= L[i]
    i+=1

print(f"Soma dos pares: {soma}")
print(f"Produto dos impares: {produto}")