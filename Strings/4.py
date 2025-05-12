'''Escreva um programa que reconhece se uma string é um palíndromo.
Exemplo: arara, ovo, reter.'''

string=input('Digite a palavra para verificar se eh um palindromo: ')

i=0
j=len(string)-1
eh_palindromo = True
while i < len(string) and eh_palindromo and i < j:
    if string[i]!= string[j]:
        eh_palindromo = False
    i+=1
    j-=1
if eh_palindromo:
    print("Palindromo")
else:
    print("Not Palindromo")