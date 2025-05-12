def soma(n1,n2):
    return n1+n2 #retorna um valor q é produzido dentro da função
def subtrai(n1,n2):
    res = n1-n2
    return res
def divide(n1,n2):
    if n2!=0:
        return n1/n2 

#--MAIN--#
num1=int(input('valor 1: '))
num2=int(input('valor 2: '))

result = soma(num1,num2)#chamando a função soma()
print(f'soma= {result}')

result = subtrai(num1,num2)
print(f'subtração = {result}')

result = divide(num1,num2)
if result == None:
    print('Não existe divisão por zero')
else: 
    print(f"Divisao:{result} ")
