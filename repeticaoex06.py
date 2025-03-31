'''Faça um programa em Python que receba dois valores inteiros,
representando a base e o expoente. O programa deverá calcular e
apresentar o resultado da base elevada ao expoente. Por exemplo, para
base = 5 e expoente = 3, ou seja, 5 3, o programa deverá imprimir 125.
Obs: não utilize o operador de exponenciação (**). Utilize somente estrutura de
repetição.'''

base = int(input("digite a base "))
exp=int(input("digite o expoente "))
result= base 
cont=1

while cont < exp: 
    result = result * base 
    cont+=1
print(f"{base} ^ {exp} = {result}")

