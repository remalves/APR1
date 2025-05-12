'''Escreva um programa que solicite ao usuário a entrada de um número
inteiro positivo ou negativo e mostre a quantidade de dígitos desse
número.'''

numero = input("Digite um numero inteiro e positivo ou negativo: ")
digitos = '0123456789'

cont=0
if numero[0] == '-':
    i = 1
    while i < len(numero):
        if numero[i] in digitos: 
            cont+=1
        i+=1
else:
    i=0
    while i < len(numero):
        if numero[i] in digitos:
            cont+=1
        i+=1
        
print(f'total de digitos: {cont}')           

