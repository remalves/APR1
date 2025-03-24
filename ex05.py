

a = float(input("Digite o valor de A: "))
if a!=0:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    delta = b**2 - (4*a*c)

    if delta < 0:
        print("Sem raíz real")

    elif delta == 0:
        x1= (-b)/ (2*a)
        print(f"valor de x: {x1:.2f}")

    else:
        import math
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta))/ (2*a)
        print(f"x1= {x1:.2f} e x2={x2:.2f}")

else:
    print("valor de a não pode ser zero")