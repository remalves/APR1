def soma(n1,n2):
    return n1+n2    
def subtrai(n1,n2):
    return n1-n2
def divide(n1,n2):
    if n2 != 0:
        return n1/n2
    else: 
        return None #indica que nao conseguiu realizar a divisao
def multiplica(n1,n2):
    return n1*n2
def potencia(n1,n2): 
    return n1**n2
def raiz_quadrada(n1):
    import math
    return math.sqrt(n1)
def porcentagem(n1,n2):
    produto = multiplica(n1,n2)
    porc = divide(produto,100)
    return porc
   

def menu():
    print("Calculadora: ")
    print("Menu de opções: ")
    print("")
    print("1-Adição")
    print("2-Subtração")
    print("3-Divisão")
    print("4-Multiplicação")
    print("5-Exponenciação")
    print("6-Raiz quadrada")
    print("7-Porcentagem")
    opcao = int(input("Escolha uma operação entre 1 e 7, ou digite 8 para encerrar: "))
    return opcao

def main():
    op = 1#valor válido de inicialização
    while op != 7:
        op = menu()
        if op == 1: 
            num1 = float(input("Valor 1:"))
            num2 = float(input("Valor 2:"))
            result = soma(num1,num2) #chama a função e realiza a soma
            print(f"Soma = {result:.2f}")
        elif op == 2:
            num1 = float(input("Valor 1:"))
            num2 = float(input("Valor 2:"))
            print(f"Subtração = ",subtrai(num1,num2))
        elif op == 3: 
            num1 = float(input("Valor 1:"))
            num2 = float(input("Valor 2:"))
            result = divide(num1, num2)
            if result!=None:
                print(f"Divisao = {result}")
            else:
                print("Indefinido")
        elif op == 4:
            num1 = float(input("Valor 1:"))
            num2 = float(input("Valor 2:"))
            print(f"Multiplicação: ",multiplica(num1,num2))
        elif op == 5:
            base = float(input("Valor da base:"))
            exp = float(input("Valor do expoente:"))
            print(f"{base} ^ {exp} = {potencia(num1,num2)}")
        elif op == 6:
            num = float("Digite o valor para raiz quadrada: ")
            print("Raiz quadrada = ", raiz_quadrada(num))
        elif op == 7:
            num1=float(input("Digite o valor que deseja calcular a % : "))
            num2=float("Digite a porcentagem que deseja (nao use %): ")
            print(f'Porcentagem = {porcentagem(num1,num2):.2f}')
        elif op == 8:
            print("Encerrando o programa ...")
        else:
            print("opção inválida!")
        #op = menu()

#chamada da função main: 
main()       #inicia a execução do código







