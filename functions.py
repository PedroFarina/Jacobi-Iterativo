#Pedro Giuliano Farina
#Victor Vasconcellos Borba

def teste():
    print("ue")
    return

def gerarMatrizBase(matrizInicial, dimensao):
    matrizRetorno = [[0 for x in range(dimensao + 1)] for y in range(dimensao)]
    for i in range(0, dimensao):
        currentXValue = matrizInicial[i][i]
        matrizInicial[i][i] = 0

        for i2 in range(0, dimensao + 1):
            if(matrizInicial[i][i2] != 0):
                matrizRetorno[i][i2] = -(matrizInicial[i][i2]/currentXValue)

    return matrizRetorno

def resolverMatriz(matriz, dimensao, tolerancia):
    valoresAtuais = [0 for x in range(dimensao)]
    valoresAnteriores = [0 for x in range(dimensao)]
    quebra = False
    k = 0

    while True:
        for i in range(0, dimensao):
            if valoresAtuais[i] != 0:
                quebra |=abs(valoresAtuais[i] - valoresAnteriores[i])/abs(valoresAtuais[i]) < tolerancia
        if quebra:
           break
        else:
            k += 1
            valoresAnteriores = []
            for val in valoresAtuais:
                valoresAnteriores.append(val)
                
            for i in range(0, dimensao):
                newLinha = []
                for i2 in range(0, dimensao):
                    newLinha.append(matriz[i][i2] * valoresAnteriores[i2])
                newLinha.append(matriz[i][dimensao])
                valoresAtuais[i] = sum(newLinha)
    return [valoresAtuais, k]

def resolverMatrizInicial(matrizInicial, dimensao, tolerancia):
    matriz = gerarMatrizBase(matrizInicial, dimensao)
    return resolverMatriz(matriz, dimensao, tolerancia)
