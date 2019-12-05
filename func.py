from random import uniform
a = 1
lr = 0.009


def feedForward(horas, A, B, C, D=1, E=0):
    global a, lr
    esperado = alocaMatriz(1, C, 2)
    entrada = alocaMatriz(1, A)
    oculta = []
    saida = []
    biasO = alocaMatriz(D, B, 1)
    biasS = alocaMatriz(1, C, 1)
    matrizEO = alocaMatriz(A, B)
    matrizOS = alocaMatriz(B, C)
    '''fixando valores de entrada e esperado para testes'''
    #entrada = [[2, 2]]
    #esperado = [[10, 4]]

    '''fase de treinamento'''
    for i in range(0, E):
        if i == E/2:
            entrada = [[2.9895, 2.9895]]
        #========================feedForward========================
        oculta = proMatriz(entrada, matrizEO)
        oculta = somMatriz(biasO, oculta)
        oculta = ELU(oculta)

        saida = proMatriz(oculta, matrizOS)
        saida = somMatriz(biasS, saida)
        saida = ELU(saida)

        #========================backPropagation========================
        errSaida = erroSaida(esperado, saida)
        biasS = errBias(biasS, errSaida, saida)
        matrizOS = backPropagation(errSaida, saida, oculta, matrizOS)

        matrizT = transp(matrizOS)
        errOculta = proMatriz(errSaida, matrizT)
        matrizEO = backPropagation(errOculta, oculta, entrada, matrizEO)
        biasO = errBias(biasO, errOculta, oculta)
    print(saida)
    '''teste da ANN com valores de entrada específicos'''
    for cont, i in enumerate(horas):
        entrada = [[int(i)/10000, int(i)/10000]]
        #print(entrada)
        oculta = proMatriz(entrada, matrizEO)
        oculta = somMatriz(biasO, oculta)
        oculta = ELU(oculta)

        saida = proMatriz(oculta, matrizOS)
        saida = somMatriz(biasS, saida)
        saida = ELU(saida)
        #print(saida)
        if 9.999999 < saida[0][0] < 10.000001:
            print(f'saida {saida} na posição {cont} con entradas {entrada}')
            print('saida localizada')


def backPropagation(errOculta, saida, entrada, pesos):
    R = []
    for i in range(len(entrada[0])):
        R.append([])
        for j in range(len(saida[0])):
            R[i].append(errOculta[0][j] * derivadaELU(saida[0][j]) * lr * entrada[0][i])
    R = somMatriz(R, pesos)
    return R


def transp(pesos):
    R = []
    for i in range(len(pesos[0])):
        R.append([])
        for j in range(len(pesos)):
            R[i].append(pesos[j][i])
    return R


def proMatriz(A, B):
    R = []
    # Multiplica
    if len(A[0]) == len(B):
        for i in range(len(A)):
            R.append([])
            for j in range(len(B[0])):
                val = 0
                for k in range(len(A[0])):
                    val += A[i][k] * B[k][j]

                R[i].append(val)
    else:
        print('Matriz de dimensões incompatíveis')
    return R


def alocaMatriz(A, B, C = 0):
    R = []
    if C == 0:
        for i in range(A):
            R.append([])
            for j in range(B):
                R[i].append(uniform(0, 2))
    else:
        for i in range(A):
            R.append([])
            for j in range(B):
                R[i].append(C)


    return R


def errBias(bias, erroOculta, saida):
    R = []
    for i in range(len(saida)):
        R.append([])
        for j in range(len(saida[0])):
            R[i].append(bias[0][j] + ((derivadaELU(saida[0][j]) * erroOculta[0][j]) * lr))
    return R


def erroSaida(esperado, saida):
    R = []
    for i in range(len(saida)):
        R.append([])
        for j in range(len(saida[0])):
            R[i].append(esperado[i][j] - saida[i][j])
    return R


def derivadaELU(A):
    if A >= 0:
        A = 1
    else:
        A = ((a ** A) - 1)
    return A


def ELU(A):
    for cont, i in enumerate(A[0]):
        if i < 0:
            A[0][cont] = ((a**i) - 1)
    return A


def somMatriz(A, B):
    R = []
    for i in range(len(A)):
        R.append([])
        for j in range(len(A[0])):
            R[i].append(A[i][j] + B[i][j])
    return R
