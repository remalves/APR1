'''Faça um programa que leia um número inteiro  0 e calcule o seu
fatorial.'''

num = int(input("Digite um numero: "))
if num == 0:
    print("fatorial de zero eh 1")
elif num >0:
    cont = num 
    fatorial = 1 

    while  cont > 1: 
        fatorial=fatorial*cont

        cont-=1

    print(f"fatorial de {num} = {fatorial}")
else: 
    print("numero invalido")
    