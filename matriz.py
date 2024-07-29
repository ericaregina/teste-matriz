teste = [[1,2,3], [4,6], [7,8,9]]

print ('Quantidade de linhas da matriz teste1', end=': ')
print(len(teste))


i=0
for lin in teste:
    print('Quantidade de elementos na linha', i, end=': ')
    print(len(lin))
    i+=1
