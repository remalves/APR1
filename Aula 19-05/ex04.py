'''Crie uma função que receba como parâmetro 
número inteiro. A função deve retornar um número
inteiro, conforme a seguir:
1. Retornar 1 se o número recebido é positivo
2. Retornar -1 se o número recebido é negativo
3. Retornar 0 se o número recebido é zero'''

def inteiro(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

    
def main():
    n = int(input("Digite um numero inteiro: "))
    print(inteiro(n))

main()