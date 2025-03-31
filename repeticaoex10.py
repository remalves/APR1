'''aça um programa que receba um número N fornecido pelo usuário e
mostre os N termos da série a seguir. Depois, imprima a soma total da
série.'''

n=int(input("informe a quantidade de termos da serie: "))
numerador = 1
denominador = 1 
soma = 0
print("S = ", end = '')

while numerador <= n:
    if numerador == n:
        print(f"{numerador}/ {denominador} ")
    else: 
        print(f"{numerador}/ {denominador} ", end = ' ')
    soma+= numerador/ denominador 
    numerador+=1
    denominador+=2

print(f"soma total = {soma:.2f}")

