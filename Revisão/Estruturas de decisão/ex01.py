
D =int(input("Digite a distancia que o robo arremessou: "))
cesta = 0

if D>=0 and D<=2000:
    if D<= 800:
        cesta = 1 
    elif D>800 and D<=1400:
        cesta = 2
    else:
        cesta = 3 
else:
    print("Numero invalido ... encerrando o programa")
    
print(f"pontos do lançamento: {cesta}")