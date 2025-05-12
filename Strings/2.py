string = input("Entre com a string: ")
letra = input("Qual letra deseja remover: ")
nova_string = ''

i=0
while i < len(string):
    if string[i] != letra: 
        nova_string += string[i] 
    i+=1

if nova_string != '':
    print(nova_string)
else:
    print("letra not found")

