'''Faça um programa que mostre os 8 primeiros termos da sequência de
Fibonacci. Ex: 0, 1, 1, 2, 3, 5, 8,13, 21,34, 55...'''

ultimo = 1
penultimo = 0
print(penultimo,ultimo)

cont = 0

while cont < 6: 
    novo_termo= penultimo +ultimo
    print(novo_termo)
    penultimo = ultimo
    ultimo = novo_termo
    
    cont+=1
