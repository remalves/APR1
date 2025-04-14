contatos = []
continuar = 'sim'

while continuar == 'sim' or continuar == 'Sim': 
    pessoa = []

    nome = input("Entre com o nome de contato: ")
    pessoa.append(nome)

    fone=input("entre com o telefone: ")
    pessoa.append(fone)

    cidade = input("entre com a cidade: ")
    pessoa.append(cidade)

    contatos.append(pessoa)

    continuar = input("Digite sim ou Sim para incluir outro contato: ")

print(contatos)



