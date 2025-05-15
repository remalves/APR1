def criar_lista(lista, qtde):
    i = 0
    while i < qtde: 
        print(f"digite {qtde} valores inteiros: ")
        num = int(input())
        lista.append(qtde)
        i+=1

def imprimir_lista(lista):
    for i in range(len(lista)):
        print(lista[i],end='')

def main():
    l1 = []
    l2 = []
    qtde = int(input("informe um numero de elementos da lista: "))
    #chamada da função criar_lista
    criar_lista(l1, qtde)
    criar_lista(l2, qtde)
    imprimir_lista(l1)
    imprimir_lista(l2)

main()