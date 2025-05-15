def double_stuff(lista):
    copia_lista = lista[:]
    for posicao in range(len(lista)):
         copia_lista[posicao] = 2 * lista[posicao]
    return copia_lista

def main():
    things = [2, 5, 9]
    print(things)
    #chamada da função enviando a lista por parametro
    #double_stuff(things)
    #print(things)
    l = []
    l = double_stuff(things)
    print(things)
    print(l)
   
main()