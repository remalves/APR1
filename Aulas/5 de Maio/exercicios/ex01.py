'''Escreva um programa que remove a primeira ocorrência de uma letra de
uma string. A string e a letra devem ser fornecidas pelo usuário.'''
palavra=input("Digite uma palavra: ")
letra_ser_removida=input("Digite uma letra a ser removida: ")
palavra_nova = " "
for letra in palavra:
    if letra != letra_ser_removida: 
        palavra_nova = palavra_nova + letra
print(palavra_nova)




