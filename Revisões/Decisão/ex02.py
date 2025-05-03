par = 0
impar = 0
P = 0
D_1 = 0
D_2=0

print("Determine o valor de P, entre 0 e 1: ")
P = int(input("Valor: "))
if P != 0 and P != 1: 
    print("Valor de P inválido ... encerrando o programa: ")

D_1= int(input("Dedos estendidos de Alice: "))
D_2= int(input("Dedos estendidos de Bob: "))

soma_dedos = 0
if D_1>=0 and D_1<=5 and D_2 >= 0 and D_2<=5:
    soma_dedos = D_1 + D_2 
    if soma_dedos % 2 == 0:
        if P == 0: 
            print(P)
        else:
            print(P)
else: 
   print("Valor de Dedos estendidos inválido ... encerrando o programa: ") 
        
        


 


