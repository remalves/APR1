contatos = [['pedrinho', '14 99999999'], ['juca', '17 92299897'], ['paula','16 31239718'],['Aurora', '16 81125569']]

i=0
while i < len(contatos):
    print(f"{contatos[i][0]}: {contatos[i][1]} ")
    i+=1

i=0

while i < len(contatos): 
    print(f"informe a cidade do {contatos[i][0]}")
    cidade = input()
    contatos[i].append(cidade)
    i+=1

for i in range(len(contatos)):
    print(f"{contatos[i][0]}: {contatos[i][1]}, {contatos[i][2]}")