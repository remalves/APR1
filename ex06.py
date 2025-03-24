valorCompra = float(input("Digite o valor total gasto: "))

if valorCompra >=200:
    novo_valor = valorCompra * 0.8 
elif valorCompra > 100: 
    novo_valor = valorCompra*0.9
else:
    novo_valor = valorCompra*0.95

print(f"valor com desconto: {novo_valor}")


