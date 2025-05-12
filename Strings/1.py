string = input("Entre com a string: ")
letra = input("Qual letra deseja remover: ")
nova_string=''

i=0
achou = False
while i < len(string) and not achou:
    if letra == string[i]:
        achou = True
        pos = i
    i+=1
if achou: 
    nova_string += string[:pos] + string[pos+1:]
    print(nova_string)
else:
    print("letra not found")