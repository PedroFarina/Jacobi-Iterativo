#Pedro Giuliano Farina
#Victor Vasconcellos Borba

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
print("Sua matriz resultante é esta:")
for i in range(0, dimensao):
    currentXValue = matriz[i][i]
    matriz[i][i] = 0
    
    for i2 in range(0,dimensao + 1):
        if(matriz[i][i2] != 0):
            matriz[i][i2] = -(matriz[i][i2]/currentXValue)
        print(str(matriz[i][i2]), end = " ")
    print()

valoresAtuais = [0 for x in range(dimensao)]
valoresAnteriores = [0 for x in range(dimensao)]
quebra = False
k = -1

while True:
    k += 1
    for i in range(0, dimensao):
        if valoresAtuais[i] != 0:
           quebra |= abs(valoresAtuais[i] - valoresAnteriores[i])/abs(valoresAtuais[i]) < tolerancia
    if quebra:
        break
    else:
        valoresAnteriores = []
        for val in valoresAtuais:
            valoresAnteriores.append(val)

        for i in range(0, dimensao):
            newLinha = []
            for i2 in range(0, dimensao):
                newLinha.append(matriz[i][i2] * valoresAnteriores[i2])
            newLinha.append(matriz[i][dimensao])
            valoresAtuais[i] = sum(newLinha)

print("Após " + str(k) + " iterações, chegamos a seguinte conclusão")    
for i in range(0, dimensao):
    print("x" + str(i + 1) + " = " + str(valoresAtuais[i]))
