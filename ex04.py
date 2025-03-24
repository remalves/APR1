a =int(input("Digite o primeiro valor: "))
b =int(input("Digite o segundo valor: "))
c =int(input("Digite o terceiro valor: "))

if a+b>c and b+c>a and a+c>b: 
    print("é um triangulo!")

    if a == b and b == c: 
        print("equilatero")
    elif a == b or b == c or a == c:
        print("isoceles")
    else:
        print("escaleno")
    
else:
    print("Não é um triangulo.")