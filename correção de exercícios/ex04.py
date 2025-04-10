N = int(input("Informe a quantidade de elementos: "))

l_original =[]
i=0
while i < N:
    num =int(input("entre com a nota: "))
    l_original.append(num)
    i+=1

sem_repeticao=[]
repetidos=[]

i=0
while i < len(l_original):
    #se a lista sem repetiçao for vazia
    #insere o elemento da lista original na lista sem repeticao
    if len(sem_repeticao) == 0:
        sem_repeticao.append(l_original[i])
    else: 
        achou = False 
        j=0 
        while j < len(sem_repeticao)and not achou: #not achou é igual achou==false
            if sem_repeticao[j]==l_original[i]:
                achou = True
            j+=1
#se encontrou o valor na lista sem_repeticao, insere na lista repetidos
        if achou: #achou == True #se não é verdade que achou pula pro else
            repetidos.append(l_original[i])
        else: 
            #se não encontrou na lista sem repetição, então insere
            sem_repeticao.append(l_original[i])
    i+=1

i=0
print("Elementos da lista original")
while i < len(l_original):
    print (l_original[i], end=' ')
    i+=1
print()

i=0
print("Elementos da lista sem repeticao")
while i < len(sem_repeticao):
    print (sem_repeticao[i], end=' ')
    i+=1
print()

i=0
print("Elementos da lista de repetidos")
while i < len(repetidos):
    print (repetidos[i], end=' ')
    i+=1
print()

