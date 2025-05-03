
C = int(input("Numero de competidores (1-1000): "))

if C>=1 and C<=1000:   
    
    P = int(input("Numero de folhas compradas: "))
    if P>=1 and P<=1000:
        
        F = int(input("Numero de folhas para cada competidor: ")) 
        if F>=1 and F<=1000:
            div =  P//C
            if div >= F:
                print("S")
            else:
                print("N")
else:
    print("Numero invalido de competidores ... encerrando o programa")
    

