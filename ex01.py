'''Elabore um programa que efetue a soma de todos os números ímpares que são
múltiplos de 3 e que se encontram no intervalo de 1 a 500'''

i=1
soma=0
impares=[]
multiplos=[]

while i <= 5:
    if i % 3 == 0:
        multiplos.append(i)
    i+=1

i=0
par = 0
while i < len(multiplos):
    if multiplos[i]%2==0:
        par+=1
    else:
        impares.append(multiplos[i])
    i+=1

soma = 0
i=0

while i < len(impares):
    soma = impares[i]+soma
    i+=1

print(soma)

    

