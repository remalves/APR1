'''Elabore a função Real(n) que verifica se o valor de entrada é um número 
real e retorna TRUE em caso afirmativo e FALSE caso contrário.'''
def real(n):
    try:
        num = float(n)
        return True
    except:
        return False
    
def main():
    n = input("Informe um valor: ")
    if real(n):
        print("eh um numero real")
    else:
        print("nao eh um numero real")
        
main()