a = ['Ana Maria Alves', 'ADS', 'sc1305370',18, 2019, [9.0,8.5,5.5,7.5,10.0]]

print('nome do aluno: ', end='')
print(a[0])

print('prontuario: ', end='')
print(a[2])

print('curso: ', end='')
print(a[1])

print(f"idade: {a[3]}")

print(f"ano de ingresso: {a[4]} ", end='')


print('boletim de notas: ')
i=0
while i<len(a[5]):
    print(a[5][i])
    i+=1
