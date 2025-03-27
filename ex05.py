'''Faça um programa que receba um número inteiro maior que 1,
verifique se o número é primo ou não e mostre a mensagem de
número primo ou de número não primo. Obs: Um número é primo
quando é divisível apenas por 1 e por ele mesmo.'''

number = int(input("Digite um numero maior que 1 e descubra se é primo: "))

while number <= 1: 
    number = int(input("Digite um numero maior que 1: "))

if number % 2 == 0:
    print(f"o numero {number} nao eh primo")

else:
    print(f"o numero {number} é primo")
    
    




    




