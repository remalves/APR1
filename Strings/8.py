frase = input('Digite uma frase: ')
vogais = 'aeiouAEIOU'
cont_vogais = 0
cont_espacos = 0
i=0
while i < len(frase):
    if frase[i] == '':
        cont_espacos+=1
        
    achou = True
    while achou: 
        if frase[i] == vogais:



    
  
print(f'Quantidade de vogais: {cont_vogais} e espaços: {cont_espacos}')

