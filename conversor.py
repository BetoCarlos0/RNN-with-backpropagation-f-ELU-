from operator import itemgetter


def conversor():
    '''formatação dos dados em 'raw' para raw.txt trabalhando com a coluna de horas 'line[1]' '''
    horas = []
    arqRead = open('raw', 'r')
    arqWrite = open('raw2.txt', 'w')

    for line in arqRead:
        if 'D009' in line:
            #print(line.split())
            #line = line.replace('-', '')
            line = line.replace(':', '')
            line = line.replace('.', ' ')
            line = line.split()
            del line[2]
            aux = line[1]
            line[1] = str((int(line[1][:2]) * 3600)+(int(line[1][2:4]) * 60) + int(line[1][4:6]))
            line.insert(1, aux)
            line = ' '.join(line)
            arqWrite.write(line + '\n')
        if '2009-02-10' in line:
            break

    arqRead.close()
    arqWrite.close()


def analise():
    '''em desenvolvimento da lógica para pegar as horas com maior frequencia durante o dia'''
    texto = []
    arqRead = open('raw2.txt', 'r')

    for line in arqRead:
        line = line.split()
        line[1] = int(line[1])
        texto.append(line)

    arqRead.close()

    matrix_ord = sorted(texto[:], key=itemgetter(1))
    #for i in matrix_ord:
    #    print(i)

    count = []
    k = 0
    for i in range(len(texto)):
        if 'D009' in texto[i] and 'OPEN' in texto[i]:
            aux = 0
            for j in range(i - 20, i + 20):
                if 'D009' in texto[j]:
                    aux += 1
            if aux >= 6:
                for k in range(i - 20, i + 20):
                    print(texto[k])
                print('\n')

