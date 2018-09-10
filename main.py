#Pedro Giuliano Farina
#Victor Vasconcellos Borba

import functions

dimensao = int(input("Defina a dimensão da matriz\n"))

matriz = [[0 for x in range(dimensao + 1)] for y in range(dimensao)]
resultados = []

for i in range(0, dimensao):
    for i2 in range(0, dimensao):
        print("Defina o coeficiente da variável x" + str(i2 + 1) + " na linha " + str(i + 1))
        matriz[i][i2] = float(input())
    print("Defina o resultado da linha")
    matriz[i][dimensao] = -float(input())
                      
tolerancia = float(input("Defina a tolerancia mínima\n"))
matriz = functions.gerarMatrizBase(matriz, dimensao)

print("Sua matriz resultante é esta:")
for i in range(0, dimensao):
    for i2 in range(0,dimensao + 1):
        print(str(matriz[i][i2]), end = " ")
    print()

resposta = functions.resolverMatriz(matriz, dimensao, tolerancia)
valores = resposta[0]
k = resposta[1]

print("Após " + str(k) + " iterações, chegamos a seguinte conclusão:")    
for i in range(0, dimensao):
    print("x" + str(i + 1) + " = " + str(valores[i]))
