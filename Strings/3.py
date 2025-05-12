'''Escreva um programa que verifique se duas strings fornecidas pelo
usuário são iguais e mostre o total de caracteres de cada uma delas.
Diferencie letras maiúsculas das minúsculas.'''

str1 = input("Digite a primeira palavra: ")
str2 = input("Digite a segunda palavra: ")

if str1 == str2: 
    print("As palavras são identicas")
else:
    print("As Palavras são diferentes")

contador=0
while contador< len(str1):
    contador+=1

i=0
while i < len(str2):
    i+=1

print(f"Tamanho da primeira palavra = {contador}")
print(f"Tamanho da segunda palavra = {i}")