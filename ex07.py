# Faça um programa em Python que leia um conjunto de valores
# correspondentes às notas que os alunos obtiveram em uma prova de
# Algoritmos. Quando o valor fornecido for um número negativo, significa
# que não existem mais notas para serem lidas. Após isso seu programa
# deverá:
#  Escrever quantas notas são maiores ou iguais a 6.0
#  Escrever quantas notas são maiores ou iguais a 4.0 e menores que 6.0
#  Escrever quantos notas são menores que 4.0
#  Escrever a média das notas fornecidas pelo usuário.

count_notas_altas=0
count_notas_medias=0
count_notas_baixas=0

nota = 0

total_notas = 0
media_notas=0

enter_nota=float(input("Digite todas as notas da turma: "))

valor_notas = 0

while enter_nota > -1: 
    
    total_notas += 1

    if enter_nota>= 6: 
        count_notas_altas+= 1

    elif enter_nota >=4:
        count_notas_medias += 1

    else: 
        count_notas_baixas+=1
    
    valor_notas = valor_notas + enter_nota  
    enter_nota = float(input("Digite todas as notas da turma: "))



media_notas = valor_notas / total_notas 


print(f"Notas maiores ou iguais a 6.0: {count_notas_altas}")
print(f"Notas maiores ou iguais a 4.0 e menores que 6.0: {count_notas_medias}")
print(f'Notas menores que 4.0: {count_notas_baixas}')    
print(f'Média das notas fornecidas pelo usuário:{media_notas}')