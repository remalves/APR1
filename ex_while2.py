'''Faça um programa que exiba todos os números de 1 a 100 que são
divisíveis por 7 e por 3.'''

i = 0
num = 0

while i <= 100:
    if num % 7 == 0 and num % 3 == 0:
        print(num)
    i = i+1
    num = num + 1