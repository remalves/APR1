palavra=input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
str_sem_vogais=""
for cada_letra in palavra:
 if cada_letra not in vogais:
    str_sem_vogais = str_sem_vogais + cada_letra
    print(str_sem_vogais)
print(palavra)
