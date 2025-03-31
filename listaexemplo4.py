cavalheiros = []

i=0
#preenchendo a lista a partir de valores informados pelo usuário

while i<4:
    nome = input("Digite um cavalheiro: ")
    cavalheiros.append(nome)
    i+=1

# imprimindo a lista
i=0
while i < len(cavalheiros):
    print(cavalheiros[i])
    i+=1
