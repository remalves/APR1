idade = int(input("Digite a idade do eleitor: "))

if idade > 15 and idade <= 17:
    print("VOTO FACULTATIVO")
    
elif idade >= 18 or idade <=65:
    print("Voto obrigatório")
    
else:
    print("Não precisa votar")

print("Fim do programa.")