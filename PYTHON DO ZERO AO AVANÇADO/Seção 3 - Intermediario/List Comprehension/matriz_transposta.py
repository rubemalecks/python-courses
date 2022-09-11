matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

transposta = []
matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# exemplo 1
for i in range(len(matriz[0])):
    l_transposta = []

    for l in matriz:
        l_transposta.append(l[i])
    transposta.append(l_transposta)
print(transposta)
for lin in transposta:
    print(lin)
# exemplo 2

transposta = [[l[i] for l in matriz] for i in range(len(matriz[0]))]
print(transposta)

print(str(zip(*matriz)))
