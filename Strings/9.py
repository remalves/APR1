str1 = input("Digite a primeira palavra: ")
str2 = input("Digite a segunda palavra: ")

str1 = str1.lower().replace('', '') #converte pra minuscula 
str1 = str1.lower().replace('', '')

if len(str1) == len(str2): #tem que ter o mesmo comprimento
    eh_anagrama=True
    i=0
    while i < len(str1) and eh_anagrama: 
        cont_str1=0 #conta quantas vezes a letra da posição i de str1 ocorre em str1 
        cont_str2=0 #conta quantas vezes a letra da posição i de str1 ocorre em str2 
        for j in range(len(str1)):
            if str1[i] == str1[j]: 
                cont_str1 += 1
        j=0
        while j < len(str2): 
            if str1[i] == str2[j]:
                cont_str2 += 1
            j+=1
          
        if cont_str1 != cont_str2: 
            eh_anagrama = False
        i+=1 
    if eh_anagrama:
        print("É um anagrama")
    else:
        print("Não é um anagrama")
else: 
    print("Não é um anagrama")