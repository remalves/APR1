# Faça um programa em Python que receba dois valores inteiros,
# representando a base e o expoente. O programa deverá calcular e
# apresentar o resultado da base elevada ao expoente. Por exemplo, para
# base = 5 e expoente = 3, ou seja, 53, o programa deverá imprimir 125.
#  Obs: não utilize o operador de exponenciação (**). Utilize somente estrutura de
# repetição.

base = int(input("Digite o numero da base: "))
expoent = int(input("Digite o numero do expoente: "))

print(f"base = {base}, expoente = {expoent}") 

valorElevado = 1

while expoent > 0: 
    valorElevado = valorElevado * base
    expoent = expoent - 1 

print(f"resultado = {valorElevado:.2f}")
