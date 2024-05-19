# 1

class Camiseta:
    def _init_(self, n, c, t):
        self.nome = n
        self.cor = c
        self.tamanho = t


def comp(a, b):
    if(a.cor == b.cor):
        if(a.tamanho == b.tamanho):
            if(a.nome < b.nome):
                return -1
            if(a.nome > b.nome):
                return 1
            return 0
        if(a.tamanho > b.tamanho):
            return -1
        return 1
    if(a.cor < b.cor):
        return -1
    return 1


def particao(V, inicio, fim):
    pivo = V[fim - 1]
    i = inicio
    for j in range(inicio, fim):
        if(comp(V[j], pivo) < 0):
            V[j], V[i] = V[i], V[j]
            i += 1

    if(comp(pivo, V[i]) < 0):
        V[fim - 1], V[i] = V[i], V[fim - 1]

    return i


def quickSort(V, inicio, fim):
    if(fim > inicio):
        posicaoPivo = particao(V, inicio, fim)
        quickSort(V, inicio, posicaoPivo)
        quickSort(V, posicaoPivo + 1, fim)


first = True
while True:
    try:
        N = int(input())

        if(N == 0):
            break

        if(first):
            first = False
        else:
            print('')

        camisetas = []
        for _ in range(N):
            nome = input()
            cor, tamanho = input().strip().split(' ')

            camisetas.append(Camiseta(nome, cor, tamanho))

        quickSort(camisetas, 0, len(camisetas))

        for camiseta in camisetas:
            print(f'{camiseta.cor} {camiseta.tamanho} {camiseta.nome}')
    except EOFError:
        break






# 2

def processar_dados_arvores():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')  
    
    caso_total = int(data[0]) 
    indice = 1
    
    resultados = []
    
    for _ in range(caso_total):
        contagem_especies = {} 
        total_arvores = 0
        
        
        if data[indice] == '':
            indice += 1
        
       
        while indice < len(data) and data[indice].strip():
            especie = data[indice].strip()  
            if especie in contagem_especies:
                contagem_especies[especie] += 1 
            else:
                contagem_especies[especie] = 1  
            total_arvores += 1 
            indice += 1  
        
       
        resultado_caso = []
        for especie in sorted(contagem_especies): 
            percentual = (contagem_especies[especie] / total_arvores) * 100   
            resultado_caso.append(f"{especie} {percentual:.4f}")  
        
        resultados.append('\n'.join(resultado_caso))  
        
        indice += 1  
    
   
    print('\n\n'.join(resultados))

if __name__ == "__main__":
    processar_dados_arvores()




# 3


import sys
import math

def calcular_area_rampa(N, H, C, L):
    base = N * C
    altura = N * H
    hipotenusa = math.sqrt(base**2 + altura**2)
    area_cm2 = hipotenusa * L
    area_m2 = area_cm2 / 10000
    return area_m2

def main():
    input = sys.stdin.read
    data = input().strip().split()
    
    i = 0
    resultados = []
    while i < len(data):
        N = int(data[i])
        H = int(data[i + 1])
        C = int(data[i + 2])
        L = int(data[i + 3])
        i += 4
        
        area_m2 = calcular_area_rampa(N, H, C, L)
        resultados.append(f"{area_m2:.4f}")
    
    for result in resultados:
        print(result)

if __name__ == "__main__":
    main()
