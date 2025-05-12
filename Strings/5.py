frase=input('Digite uma frase: ')
frase = frase.strip()
cont=0
i=0
while i < len(frase):
    if frase[i] == ' ': 
        cont+=1
    i += 1
print(f"Total de palavras da frase = {cont+1}")
