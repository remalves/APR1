def inteiroPositivo(v):
    try:
        retorno = int(v)
        if retorno >= 0:
            return True
        else:
            return False 
    except: 
        return False

def fatorial(num):
    i = 1
    n = int(num)
    fat = 1
    while i <= n:
        fat*=i
        i+=1
        
    return fat
                  
def main():
    v = input("Digite um valor: ")
    if inteiroPositivo(v): #chama a função
        print('fatorial = ' , fatorial(v))
    else:
        print(f"o valor {v} não é um inteiro e positivo")
        
main()