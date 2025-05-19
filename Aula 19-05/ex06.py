'''Faça uma função que receba quatro valores, referentes 
as notas que um aluno obteve nos bimestres. 
A função deve retornar Verdadeiro se o aluno 
foi aprovado e Falso caso contrário. '''

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
    mediaf=soma/len(notas)
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
                    
    if media(notas) >= 6:
        return print('True')
    else:
        return print('False')
main()                    