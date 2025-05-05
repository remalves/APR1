frase = "Eu posso ajudar respondendo perguntas no forum!"
sorteio=[5,-4,3,-8,11]
acertos = 0 
for i in sorteio:
    resposta = input(f"Qual o caractere do indice {i}: ")
    if frase[i] == resposta:
        print("Parabens, voce acertou!")
        acertos+=1
    else:
        print(f"Voce errou. O caractere de indice {i} é: {frase[i]} ")

print(f"Voce acertou {acertos} de {len(sorteio)} perguntas. ")