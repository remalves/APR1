nome=input('Digite seu nome: ')
nome = nome.upper()
i=-1

while i >= -len(nome): 
    print(nome[i], end='')
    i-=1

print()