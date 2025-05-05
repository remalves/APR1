'''ss = " Hello, World "
els = ss.count("l") #retorna o numero de ocorrencias de um item 
print(els)    
print("***"+ss.strip()+"***") #retorna uma string removendo caracteres em branco do inicio e do fim    
print("***"+ss.lstrip()+"***") #retorna uma string removendo caracteres em branco do inicio   
print("***"+ss.rstrip()+"***")#retorna uma string removendo caracteres em branco do fim
news = ss.replace("o", "***")#substitui a ocorrencia da substring old por new (troca O por ***)
print(news)'''

ss = "Hello, World"
print(ss.upper())
tt = ss.lower()
print(tt)

ss2 = " Hello, World "
els = ss2.count("l")
print(els)

print("***"+ss2.strip()+"***")
print("***"+ss2.lstrip()+"***")
print("***"+ss2.rstrip()+"***")
news = ss2.replace("o", "***")
print(news)

