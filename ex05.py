num = int(input("Informe um numero inteiro: "))
i = 2
primo = True

while i < num and primo == True: 
    if num % i == 0:
        primo = False
    i+=1

if primo == True:
    print("O número eh primo")
else:
    print("Nao eh primo")