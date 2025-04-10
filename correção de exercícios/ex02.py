N = int(input("Informe a quantidade de notas: "))

soma = 0
notas =[]
i=0
while i < N:
    nota=float(input("entre com a nota: "))
    #verificar se a nota está entre 0 - 10
    while nota < 0 or nota>10:
        nota=float(input("entre com a nota: "))
    notas.append(nota)
    i+=1

i=0
soma=0
while i < len(notas):
    soma+=notas[i]
    i+=1
while i < len(notas): 
    print(notas[i], end=' ')
    i+=1
    
print() #faz papel de enter 

print(f"media notas:{soma/N:.2f}")
