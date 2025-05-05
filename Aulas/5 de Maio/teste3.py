ini,fim=3,7
texto= "Eu posso ajudar respondendo perguntas no forum!"
fatia = texto[ini:fim]
print("Seja o texto: ", texto)
resposta=input(f"Digite a string que corresponde a fatia de texto [{ini}:{fim}]: ")
if resposta == fatia:
    print("Muito bem, você acertou!")
else:
    print("Voce escreveu: ", resposta)
    print("Mas o valor correto é: ", fatia)