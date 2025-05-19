'''Faça uma função que receba quatro valores reais
(faça a consistência), referentes as notas que 
um aluno obteve nos bimestres. 
A função deve retornar a 
média final desse aluno. 
Pesquise como arredondar a nota'''

def real(n):
    try:
        num = float(n)
        return True
    except:
        return False

def media(notas):
    soma = 0
    for i in range(len(notas)): 
        soma+=notas[i] 
    mediaf=soma/4    
    return round(mediaf,2)

def main():
    notas = []
    count = 0
    while count < 4: 
            n = input(f"Nota {count+1}: ")
            if real(n):
                num = float(n)
                if num >= 0 and num <= 10:
                    notas.append(num)
                    count+=1
                else:
                    print("Digite um valor válido ...")                  
    print(f"Media final: {media(notas)}")
main()
    


    