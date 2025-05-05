food = "banana bread"
print(food.capitalize()) #a primeira string em maiuscula e o resto em minuscula
print("*"+food.center(25)+"*")#centraliza a string
print("*"+food.ljust(25)+"*")#alinha a esquerda
print("*" +food.rjust(25)+"*")#alinha a direita
print(food.find("e")) #retorna o indice mais a esquerda onde o item e encontrado
print(food.find("na")) 
print(food.find("b"))
print(food.rfind("e"))
print(food.rfind("na"))
print(food.rfind("b"))#retorna o indice mais a direita onde o item e encontrado
print(food.index("e")) ##retorna o indice  onde o item e encontrado