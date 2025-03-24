'''Faça um programa para mostrar a tabuada de um número qualquer
fornecido pelo usuário. Por exemplo, se o número fornecido for igual a
3, o programa de apresentar a seguinte saída:'''

num = float(input("Digite um número: "))

i = 1

while i <=10:
    resultado = num * i 

    print(f" {i} x {num} = {resultado}")

    i=i+1