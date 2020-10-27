"""
Nome: Renan de Assis
NºUSP: 9865401
"""
def pertence(item,lista):
    "Retorna True se o item estiver dentro da lista"
    
    return item in lista

def VerificaLinha(mat):
    
    for linha in mat:
        aux1 = []
        for num in linha:
            if num in aux1: return False
            elif num != 0: aux1.append(num)
    return True

def VerificaLinhaPreenchida(mat):
    
    for linha in mat:
        aux1 = []
        for num in linha:
            if num in aux1: return False
            else: aux1.append(num)
    return True
                
def VerificaColuna(mat):
    
    lins = len(mat)
    cols = len(mat[0])
    for i in range(lins):
        aux2 = []
        for j in range(cols):
            if mat[j][i] in aux2: return False
            elif mat[j][i] != 0: aux2.append(mat[j][i])
    return True

def VerificaColunaPreenchida(mat):
    
    lins = len(mat)
    cols = len(mat[0])
    for i in range(lins):
        aux2 = []
        for j in range(cols):
            if mat[j][i] in aux2: return False
            else: aux2.append(mat[j][i])
    return True

def VerificaQuad(mat):
    
    sep = [[0,1,2],[3,4,5],[6,7,8]]
    
    aux3 = []
    for i in sep[0]:
        for j in sep[0]:
            if mat[i][j] in aux3: return False
            elif mat[i][j] != 0: aux3.append(mat[i][j])
    aux3 = []        
    for i in sep[0]:
        for j in sep[1]:
            if mat[i][j] in aux3: return False
            elif mat[i][j] != 0: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[0]:
        for j in sep[2]:
            if mat[i][j] in aux3: return False
            elif mat[i][j] != 0: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[1]:
        for j in sep[0]:
            if mat[i][j] in aux3: return False
            elif mat[i][j] != 0: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[1]:
        for j in sep[1]:
            if mat[i][j] in aux3: return False
            elif mat[i][j] != 0: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[1]:
        for j in sep[2]:
            if mat[i][j] in aux3: return False
            elif mat[i][j] != 0: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[2]:
        for j in sep[0]:
            if mat[i][j] in aux3: return False
            elif mat[i][j] != 0: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[2]:
        for j in sep[1]:
            if mat[i][j] in aux3: return False
            elif mat[i][j] != 0: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[2]:
        for j in sep[2]:
            if mat[i][j] in aux3: return False
            elif mat[i][j] != 0: aux3.append(mat[i][j])
    return True

def VerificaQuadPreenchido(mat):
    
    sep = [[0,1,2],[3,4,5],[6,7,8]]
    
    aux3 = []
    for i in sep[0]:
        for j in sep[0]:
            if mat[i][j] in aux3: return False
            else: aux3.append(mat[i][j])
    aux3 = []        
    for i in sep[0]:
        for j in sep[1]:
            if mat[i][j] in aux3: return False
            else: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[0]:
        for j in sep[2]:
            if mat[i][j] in aux3: return False
            else: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[1]:
        for j in sep[0]:
            if mat[i][j] in aux3: return False
            else: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[1]:
        for j in sep[1]:
            if mat[i][j] in aux3: return False
            else: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[1]:
        for j in sep[2]:
            if mat[i][j] in aux3: return False
            else: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[2]:
        for j in sep[0]:
            if mat[i][j] in aux3: return False
            else: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[2]:
        for j in sep[1]:
            if mat[i][j] in aux3: return False
            else: aux3.append(mat[i][j])
    aux3 = []
    for i in sep[2]:
        for j in sep[2]:
            if mat[i][j] in aux3: return False
            else: aux3.append(mat[i][j])
    return True


def TestaMatrizLida(Mat):
    """Devolve True se a matriz lida (Mat) está com as casas já preenchidas com os valores corretos.
       Ou seja, se não há repetições na linha, na coluna ou no quadrado interno."""
    
    #Verificar linha
    if VerificaLinha(Mat) == False: return False
    
    #Verificar coluna
    if VerificaColuna(Mat) == False: return False
    
    #Verificar quadrado
    if VerificaQuad(Mat) == False: return False
    
    return True

def TestaMatrizPreenchida(Mat):
    "Devolve True se a matriz Mat está preenchida corretamente. False caso contrário."
    
    #Verificar linha
    if VerificaLinhaPreenchida(Mat) == False: return False
    
    #Verificar coluna
    if VerificaColunaPreenchida(Mat) == False: return False
    
    #Verificar quadrado
    if VerificaQuadPreenchido(Mat) == False: return False
    
    return True
        
def LeiaMatrizLocal(NomeArquivo):
    """A partir de um arquivo de texto retorna a matriz lida se estiver
       tudo certo ou uma lista vazia caso a matriz seja dada errada."""
        
    # Abre o arquivo para leitura
    try:
        arq = open(NomeArquivo,"r")
    except:
        return [] # retorna lista vazia se deu erro
    
    # Cria a matriz SudoKu a ser lida
    mat = [9 * [0] for k in range(9)]
    
    # Ler cada uma das linhas do arquivo
    i = 0
    for linha in arq:
        linha = linha.strip().split()
        
        #Verifica se há linha em branco
        if linha == []:
            continue
        
        # Verifica se a linha possui 9 elementos
        if len(linha) != 9: return ([])
        
        # Verifica se cada elemento da linha é um inteiro entre 0 e 9
        strings = ['0','1','2','3','4','5','6','7','8','9']
        for elem in linha:
            if not pertence(elem,strings): return ([])
            
        # Percorre cada elemento da linha e coloca na matriz
        for j in range(len(linha)): mat[i][j] = int(linha[j])
            
        #Faz as consistências iniciais da matriz dada
        if TestaMatrizLida(mat) == False: return ([])

        i = i + 1
    
    # fechar arquivo e retorna a matriz lida
    arq.close()
    return mat
    
def ProcuraElementoLinha(Mat, L, d):
    """Procura dígito d (1 ≤ d ≤ 9) na linha L da matriz Mat. 
       Devolve -1 se não encontrou ou o índice da coluna onde foi encontrado."""
    
    for i in range(len(Mat)):
        if Mat[L][i] == d: return i
    return -1

def ProcuraElementoColuna(Mat, C, d):
    """Procura dígito d (1 ≤ d ≤ 9) na coluna C da matriz Mat. 
       Devolve -1 se não encontrou ou o índice da linha onde foi encontrado."""
    
    for i in range(len(Mat)):
        if Mat[i][C] == d: return i
    return -1

def ProcuraElementoQuadrado(Mat, L, C, d):
    """Procura o dígito d (1 ≤ d ≤ 9) no quadrado interno onde está o elemento Mat[L][C].
       Devolve a dupla (k1, k2) se d está na posição Mat[k1][k2] ou (-1, -1) caso contrário."""
    
    separacao = [[0,1,2],[3,4,5],[6,7,8]]
    for teste in separacao:
        if L in teste: linha = teste
        if C in teste: coluna = teste
    for i in linha:
        for j in coluna:
            if Mat[i][j] == d:
                k1,k2 = i,j
                return (k1,k2)
    return (-1,-1)

def ProcuraCasaVazia(Mat):
    "Retorna o 1º elemento nulo (casa vazia) na matriz Mat ou retorna a tupla (-1,-1) caso não exista."
    
    for i in range(9):
        for j in range(9):
            if Mat[i][j] == 0:
                return i,j
    return -1,-1

cont = 0
    
def Sudoku(Mat, Lin, Col):
    """Função principal que preenche a matriz Sudoku, 
       verificando se chegou ao final de uma solução e retrocedendo sempre que necessário."""        
    
    if ProcuraCasaVazia(Mat) == (-1,-1):
        if TestaMatrizPreenchida(Mat) == True:
            print('\n  * * * Matriz completa * * *\n')
            Imprime_Matriz(Mat)
            print('\n  * * * Matriz completa e consistente * * *')
            global cont
            cont += 1
        return
    else:
        lin,col = ProcuraCasaVazia(Mat)
    
    candidatos = {1,2,3,4,5,6,7,8,9}
    poss_val = candidatos.difference(set(Mat[lin]))
    for cand in poss_val:
        if ProcuraElementoLinha(Mat,lin,cand) == -1 and ProcuraElementoColuna(Mat,col,cand) == -1 and ProcuraElementoQuadrado(Mat,lin,col,cand) == (-1,-1):
            Mat[lin][col] = cand
            Sudoku(Mat,Lin,Col)
            Mat[lin][col] = 0

def Imprime_Matriz(Mat):
    "A partir de uma lista retorna uma matriz (separadas em linhas e colunas) representando o jogo Sudoku."
    
    for linha in Mat:
        for coluna in linha:
            print("{}".format(coluna).rjust(3),end="")
        print()
        
from time import perf_counter

def main():
    
    fim = False
    while not fim:
                
        #Leitura do arquivo
        arq = input('Entre com o nome do arquivo ou "fim": ')
        if arq == 'fim':
            fim = True
            continue
        
        #Cria a matriz e verifica se está correta
        matriz = LeiaMatrizLocal(arq)
        if matriz == []:
            print('A matriz está incorreta. Forneça uma matriz válida ou "fim":\n')
            continue
            
        #Matriz inicial
        print('\n  * * * Matriz inicial * * *\n')
        Imprime_Matriz(matriz)

        #Resolve o Sudoku e imprime as soluções já verificadas
        global cont
        tempo1 = perf_counter()
        Sudoku(matriz,0,0)
        tempo2 = perf_counter()

        #Imprime o tempo decorrido e o número de soluções
        tempo_decorrido = tempo2 - tempo1
        print('\nTempo decorrido = {} segundos'.format(tempo_decorrido))
        print('{} soluções para essa matriz.\n'.format(cont))
        cont = 0
        
main()

