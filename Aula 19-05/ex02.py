'''Elabore a função Inteiro(n) que 
verifica se o valor de entrada é um
número inteiro e 
retorna Verdadeiro em caso afirmativo 
e Falso caso contrário.'''

def inteiro(n):
   try:
        val = int(n)
        if val > 0 or val < 0: 
            return True
        else:
            return False
   except:
       return False
    
def main():
    n = input("Digite um valor: ")
    if inteiro(n): 
        print("Eh um Numero inteiro")
    else:
        print("Não eh um numero inteiro")
main()