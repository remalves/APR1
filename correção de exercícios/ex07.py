N=int(input("Informe a quantidade de elementos: "))

lista=[]

for i in range(0,N,1): #começa em 0 e vai até N, incrementando de 1 em 1
    num = int(input("Entre com o valor: "))
    lista.append(num)


for i in range(len(lista)-1,-1,-1):
    print(lista[i])


# i=len(lista)-1 

# while i >=0: 
#     print(lista[i])
#     i-=1 #decrementa N=int(input("Informe a quantidade de elementos: "))

# lista=[]

# #outra forma: 

# i=-1
# while i >= -len(lista):
#     print(lista[i])
#     i-=1




