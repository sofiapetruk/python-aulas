#Matriz, sequência atras de sequência
#Todos os elementos tem que ter a mesma quantidade na vertical e na horizontal
'''
- **Arrays**: São coleções de elementos do mesmo tipo, com um tamanho fixo que 
é definido durante a declaração. Os elementos são acessados por meio de um índice 
numérico. - **Listas**: São coleções dinâmicas de elementos do mesmo tipo, cujo 
tamanho pode ser alterado dinamicamente durante a execução do programa.
'''

def criar_matriz(n_linhas, n_colunas): #a gente já pede os parârametros antes, pq ja sabemos que iremos utilizar em algum lugar
    matriz = []
    for i in range(n_linhas):
        linha = []  #criar outra lista para criar uma matriz de linha, depois colocar na matriz
        for j in range(n_colunas):
            n = int(input('Número: ')) #para cada número que o usuário digitar vou dar apend na linha até forma a linha da matriz para ir para a outra linha
            linha.append(n)
        matriz.append(linha) # fora do primeiro for pq ele só adiciona a coluna
    return matriz

def imprimir_matriz(matriz):
    for linha in range(len(matriz)): #devolve quantas linha tem na matriz
        for coluna in range(len(matriz[linha])): #vai pecorrer cada número da matriz, qual é o tamanho da matriz na linha; Qual é o tamanho da posição 0; Cada linha indepedente de uma da outra
            print(f'matriz[{linha}][{coluna}]: {matriz[linha][coluna]}') #uma função void, formatação com indipolador

#criar uma função que receba uma matriz por parâmetro, e retorne o somatório de todos os elementos da matriz
def soma_matriz(matriz):
    soma = 0
    for linha in range(len(matriz)): #descobrir o tamanho da matriz, quantidade linha
        for coluna in range(len(matriz[linha])): #tamanho da posição da matriz, quantidade colunas
            soma += matriz[linha][coluna]
    return soma

#Principal
matriz = criar_matriz(3, 3) #já estou fornencendo os parâmetros o 3, 3
print(matriz)
imprimir_matriz(matriz)
print(f'Soma: {soma_matriz(matriz)}')#dentro do print eu irei chamar a soma; pede uma parâmetro na função ent tem que colocar também "soma_matriz(matriz)"