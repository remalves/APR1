N=int(input("Informe a quantidade de elementos: "))

lista=[]

for i in range(0,N,1): #começa em 0 e vai até N, incrementando de 1 em 1
    num = int(input("Entre com o valor: "))
    lista.append(num)

print("Lista original: ", end=' ')
for i in range(len(lista)):
    print(lista[i])
    
print("Lista ao cubo: ", end=' ')
for i in range(len(lista)):
    print(lista[i]**3)