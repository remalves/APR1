palavra=input("Digite uma palavra: ")
caractere=input("Digite um caracter a ser encontrado: ")
indice = 0
existe_letra = False
while indice < len(palavra) and not existe_letra:
 if palavra[indice] == caractere:
    existe_letra = True
 else:
    indice = indice + 1
if existe_letra:
 print(f"A primeira ocorrência do caractere {caractere} na palavra {palavra} está na posição {indice}")
else:
 print(f"Não há ocorrência do caractere {caractere} na palavra {palavra}!")