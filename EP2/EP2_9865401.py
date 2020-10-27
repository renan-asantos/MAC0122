class PilhaLista:
    
    '''Pilha como uma lista.'''
    
    # construtor da classe PilhaLista
    def __init__(self):
        self._pilha = []
    
    # retorna o tamanho da pilha
    def __len__ (self):
        return len(self._pilha)
    
    # retorna True se pilha vazia
    def is_empty(self):
        return len(self._pilha) == 0
    
    # empilha novo elemento e
    def push(self, e):
        self._pilha.append(e)
        
    # retorna o elemento do topo da pilha sem retirá-lo, exceção se pilha vazia
    def top(self):
        if self.is_empty( ):
            raise IndexError("Pilha vazia")
        return self._pilha[-1]
    
    # desempilha elemento, exceção se pilha vazia
    def pop(self):
        if self.is_empty( ):
            raise IndexError("Pilha vazia")
        return self._pilha.pop( )
    
    # troca o elemento do topo da Pilha
    def change_top(self, val):
        self._pilha[-1] = val
        
    # imprime a pilha como uma lista
    def __str__(self):
        return str(self._pilha)
    
# dicionário que guarda as variáveis do programa principal
dicio_variaveis = {}

def prioridade(x):
    
    """Define a prioridade dos operadores que podem ser utilizados"""
    
    if x == '_': return 6
    elif x == '#': return 5
    elif x == '^': return 4
    elif x == '/': return 3
    elif x == '*': return 3
    elif x == '-': return 2
    elif x == '+': return 2
    elif x == '=': return 1
    else: return 0
    
def ArrumaExpressao(exp_inicial):
    
    """Recebe uma expressão que pode ou não conter um ou mais espaços
    entre os elementos e retorna uma lista com cada elemento separado."""
    
    # possíveis elementos da expressão
    operadores = '()_#^/*+-='
    letras = 'abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ'
    numeros = '1234567890'
    espaco = ' '
    opcoes = operadores+letras+numeros+espaco
    
    # verifica se é uma expressão vazia
    if exp_inicial == '': return []
    
    # verifica se os elementos são válidos e cria uma lista separando cada um
    exp_separada = ''
    for i in range(0,len(exp_inicial)):
        if exp_inicial[i] not in opcoes: return False
        elem_com_branco = ' '+exp_inicial[i]+' '
        exp_separada += elem_com_branco
    
    # elimina os espaços adicionais
    exp = exp_separada.split()
    
    # trata os casos excepcionais
    i = 0
    while i < len(exp):
        # variáveis com mais de um elemento
        if exp[i] not in operadores and i+1 < len(exp):
            try:
                while exp[i+1] not in operadores:
                    exp[i] = exp[i]+exp[i+1]
                    del(exp[i+1])
            except:
                break
        # unário '-'
        if exp[i] == '-':
            if i == 0:
                exp[i] = '_'
            elif exp[i-1] in operadores:
                exp[i] = '_'
        # unário '+'
        if exp[i] == '+':
            if i == 0:
                exp[i] = '#'
            elif exp[i-1] in operadores:
                exp[i] = '#'
        # exponenciação '**'
        if exp[i] == '*' and exp[i+1] == '*':
            exp[i+1] = '^'
            del(exp[i])
        i+=1
    return exp
    
def TraduzPosFixa(exp_inicial):
    
    """Traduz uma expressão da notação infixa para a pós-fixa, retorna False caso contrário."""
    
    # organiza a expressão inicial e verifica se todos os caracteres são válidos
    exp = ArrumaExpressao(exp_inicial)
    if exp == False: return False
    elif exp == []: return []
    
    # declara as variáveis
    pos_fixa = []
    operadores = '()_#^/*+-='
    P = PilhaLista()
    
    # itera sobre os elementos da expressão verificando cada caso
    for elem in exp:
        if elem not in operadores: pos_fixa.append(elem)
        elif elem == '(': P.push(elem)
        elif elem == ')':
            valor = P.pop()
            while valor != '(':
                pos_fixa.append(valor)
                valor = P.pop()
        else:
            while not P.is_empty() and prioridade(P.top()) >= prioridade(elem):
                pos_fixa.append(P.pop())
            P.push(elem)
    while not P.is_empty():
        pos_fixa.append(P.pop())
    return pos_fixa

def CalcPosFixa(listaexp):
    
    """Calcula o valor de uma expressão dada em notação pós-fixa."""
    
    # declara as variáveis
    global dicio_variaveis
    P = PilhaLista()
    operadores = '()_#^/*+-='
    letras = 'abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ'
    numeros = '1234567890'
    
    # verifica se é uma expressão vazia
    if listaexp == []: return []
    
    # iterar sob a expressão verificando cada caso
    for i in range(len(listaexp)):
        if listaexp[i] not in operadores:
            if i == 0 and '=' in listaexp:
                P.push(listaexp[i])
            elif listaexp[i] not in dicio_variaveis and not listaexp[i].isnumeric():
                return listaexp[i]
            elif listaexp[i] in dicio_variaveis:
                P.push(dicio_variaveis[listaexp[i]])
            else:
                try:
                    P.push(float(listaexp[i]))
                except:
                    P.push(listaexp[i])
        elif listaexp[i] == '_':
            P.change_top(-1*float(P.top()))
        elif listaexp[i] == '#':
            P.change_top(+1*float(P.top()))
        elif listaexp[i] == '^':
            valor2 = P.pop()
            valor1 = P.pop()
            P.push(float(valor1)**float(valor2))
        elif listaexp[i] == '/':
            valor2 = P.pop()
            valor1 = P.pop()
            P.push(float(valor1)/float(valor2))
        elif listaexp[i] == '*':
            valor2 = P.pop()
            valor1 = P.pop()
            P.push(float(valor1)*float(valor2))
        elif listaexp[i] == '-':
            valor2 = P.pop()
            valor1 = P.pop()
            P.push(float(valor1)-float(valor2))
        elif listaexp[i] == '+':
            valor2 = P.pop()
            valor1 = P.pop()
            P.push(float(valor1)+float(valor2))
        elif listaexp[i] == '=':
            valor = P.pop()
            variavel = P.pop()
            dicio_variaveis[variavel] = valor
            return None
    return P.pop()

def main():
    while True:
        exp_inicial = input('>>> ')
        exp = TraduzPosFixa(exp_inicial)
        print(exp)
        if exp == False:
            print('SyntaxError: sintaxe inválida')
            continue
        try:
            calculo = CalcPosFixa(exp)
            if type(calculo) == str: print("NameError: variável '{}' não está definida.".format(calculo))
            elif calculo == []: continue
            elif calculo != None: print(calculo)
        except IndexError: print('SyntaxError: sintaxe inválida')
main()

