'''Faça um programa que solicite o nome do usuário e imprima-o na
vertical e em formato de escada. '''

nome=input('Digite seu nome: ')

i=0
while i < len(nome):
    print(nome[:i+1])
    i+=1
