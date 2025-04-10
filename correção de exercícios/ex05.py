N = int(input("Informe a quantidade de elementos: "))

a =[]
i=0
while i < N:
    num =int(input("entre com o numero: "))
    a.append(num)
    i+=1

b =[]
i=0
while i < N:
    num =int(input("entre com a nota: "))
    a.append(num)
    i+=1


c=[]
i=0
while i<len(a):
    soma = a[i]+b[i]
    c.append(soma)
    i+=1
print ("Elementos da lista a: ", end=' ')

#imprimindo a lista com for
for i in range(len(a)): #por padrão já começa em zero 
    print(a[i])
print()

print ("Elementos da lista b: ", end=' ')
for i in range(len(b)): #por padrão já começa em zero 
    print(b[i])
print()

print ("Elementos da lista c: ", end=' ')
for i in range(len(c)): #por padrão já começa em zero 
    print(c[i])
print()