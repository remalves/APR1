'''Elabore a função InteiroPositivo(n) que verifica 
se o valor de entrada é um número inteiro positivo e 
retorna Verdadeiro em caso afirmativo e Falso caso contrário.'''
def inteiroPositivo(v):
    try:
        retorno = int(v)
        if retorno >= 0:
            return True
        else:
            return False 
    except: 
        return False
    
def main():
    v = input("Digite um valor: ")
    
    if inteiroPositivo(v): #chama a função
        print(f"o valor {v} é um inteiro e positivo")
    else:
        print(f"o valor {v} não é um inteiro e positivo")
        
main()