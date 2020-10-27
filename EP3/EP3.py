class Strings:
    
    """Classe que modifica como a string do programa deve ser comparada"""
    
    def __init__(self, strg):
        self.strg = strg
        self.strings = strg.split(',')
        self.nome = self.strings[0]
        self.data = self.strings[1].split('/')
        self.num = self.strings[2]
    
    def ComparaData(str1,str2):
        
        """Retorna True se a data da 1ª string é menor que a da 2ª"""
        
        dia1, dia2 = str1.data[0], str2.data[0]
        mes1, mes2 = str1.data[1], str2.data[1]
        ano1, ano2 = str1.data[2], str2.data[2]
        if ano1 == ano2:
            if mes1 == mes2:
                if dia1 < dia2: return True
                else: return False
            elif mes1 < mes2: return True
            else: return False
        elif ano1 < ano2: return True
        else: return False
        
    def __lt__(str1,str2):
        
        """Compara duas strings e, de acordo com as intruções,
           devolve True se a 1ª for menor que a 2ª"""
        
        if str1.nome == str2.nome:
            if str1.data == str2.data:
                if str1.num == str2.num: return True
                elif str1.num < str2.num: return True
                else: return False
            elif str1.ComparaData(str2):return True
            else: return False
        elif str1.nome < str2.nome: return True
        else: return False
        
    def __str__(self):
        return self.strg

def Particiona(lista, inicio, fim):
    
    """Particiona mudando os elementos de lugar"""
    
    i, j = inicio, fim
    pivo = lista[fim]
    while True:
        # aumentando i
        while i < j and Strings(lista[i]) < Strings(pivo): i = i + 1
        if i < j: lista[i], lista[j] = pivo, lista[i]
        else: break
        # diminuindo j
        while i < j and Strings(pivo) < Strings(lista[j]): j = j - 1
        if i < j: lista[i], lista[j] = lista[j], pivo
        else: break
    return i

def ClassQuickRecursivo(tab, inicio, fim):
    
    """Método Quick recursivo"""
    
    if inicio < fim:
        k = Particiona(tab, inicio, fim)
        ClassQuickRecursivo(tab, inicio, k - 1)
        ClassQuickRecursivo(tab, k + 1, fim)

class PilhaLista:
    
    '''Pilha como uma lista.'''
    
    def __init__(self):
        self._pilha = []
    def __len__ (self):
        return len(self._pilha)
    def is_empty(self):
        return len(self._pilha) == 0
    def push(self, e):
        self._pilha.append(e)
    def pop(self):
        if self.is_empty():
            raise IndexError("Pilha vazia")
        return self._pilha.pop()        

def ClassQuickNaoRecursivo(tab):
    
    """Método Quick Não Recursivo"""
    
    # Cria a pilha de sub-listas e inicia com lista completa
    Pilha = PilhaLista()
    Pilha.push((0, len(tab) - 1))
    # Repete até que a pilha de sub-listas esteja vazia
    while not Pilha.is_empty():
        inicio, fim = Pilha.pop()
        # Só particiona se há mais de 1 elemento
        if fim - inicio > 0:
            k = Particiona(tab, inicio, fim)
            # Empilhe as sub-listas resultantes
            Pilha.push((inicio, k - 1))
            Pilha.push((k + 1, fim))
            
def ClassMetodoSort(tab):
    
    """Método Sort do Python"""
    
    tab_nova = []
    for elem in tab:
        tab_nova.append(Strings(elem))
    tab_nova.sort()
    return tab_nova
                
def LeArquivo(arq_inicial):
    
    """Retorna o arquivo.txt no formato de uma lista"""
    
    with open(arq_inicial) as arq:
        Tab = []
        for linha in arq:
            lin = linha.strip()
            Tab.append(lin)
        return Tab
    
def VerifClass(Tab, M = 'ok'):
    
    """Verifica se a lista Tab está classificada"""
    
    if M != 'sort':
        for i in range(len(Tab)):
            if i == len(Tab)-1: return True
            if Strings(Tab[i+1]) < Strings(Tab[i]): return False
    else:
        for i in range(len(Tab)):
            if i == len(Tab)-1: return True
            if Tab[i+1] < Tab[i]: return False
        
from time import perf_counter
            
def main():
    
    while True:
        
        # arquivos de origem e destino
        arq_origem = input('Entre com o nome do arquivo de origem: ')
        if arq_origem == 'fim': break
        arq_destino = input('Entre com o nome do arquivo de destino: ')
        
        # arquivo como uma lista
        try:
            tab = LeArquivo(arq_origem)
        except FileNotFoundError:
            print("Arquivo não encontrado, digite outro ou 'fim'")
            continue
        tab1 = tab[:]
        tab2 = tab[:]
        
        print('\nQuantidade de registros a classificar: {} registros\n'.format(len(tab)))
           
        print('Tempo para classificar a tabela: ')
        
        # classificação método quick recursivo
        t1_QR = perf_counter()
        ClassQuickRecursivo(tab,0,len(tab)-1)
        t2_QR = perf_counter()
        if VerifClass(tab) == False: 
            print('Quick recursivo não classificou')
            continue
        print('Método Quick Recursivo: {} segundos'.format(t2_QR-t1_QR))
        
        # classificação método quick não recursivo
        t1_QNR = perf_counter()
        ClassQuickNaoRecursivo(tab1)
        t2_QNR = perf_counter()
        if VerifClass(tab1) == False:
            print('Quick não recursivo não classificou')
            continue
        print('Método Quick Não Recursivo: {} segundos'.format(t2_QNR-t1_QNR))
        
        # classificação método sort
        t1_SORT = perf_counter()
        nova = ClassMetodoSort(tab2)
        t2_SORT = perf_counter()
        if VerifClass(nova,'sort') == False: 
            print('Método Sort não classificou')
            continue
        print('Método sort() do Python: {} segundos\n'.format(t2_SORT-t1_SORT))
            
        # retorna o arquivo ordenado
        with open(arq_destino,'w') as arq:
            for i in nova:
                arq.write(str(i))
                arq.write('\n')
        
main()
