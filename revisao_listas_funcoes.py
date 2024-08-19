#não pedir os dados em uma função, precisamos validar primeiro o usuario e senha, não deixar o código acoplado pq precismos utilizar em vários lugares

#Evitar estruturas globais e acoplamento de estruturas
"""
O usuário vai ter quanto elementos colocar na lista
Cada funcionalidade temos uma função
"""

#Primeira funcionalidade, quantos elemento quero colocar na lista
#Não precisamos passar parâmetro, parÂmetro é a informação externa que trazemos para retornar algo
def tamanho_lista():
    print("**- Tamanho da LISTA -**") #isso é so perfurmaria, para o código ficar bonito
    print("-------------------------")
    tamanho = int(input("Tamanho da lista: "))
    return tamanho #damos retorno no tamanho pq iremos reutilizar esse tamanho em outro lugar, para quem precisar utilizar essa informação


#Vou criar uma lista, agorá iremos usar o parâmetro do tamanho da lista, por que já vamos preencher os eleemnetos da lista que o usuário irá colocar
#Quando passamos uma variável para um parârametro ela passa para a função criada, e fica no local dela
def criar_lista(tamanho):
    print(f"**- Criando uma LISTA com {tamanho} elementos")
    print("------------------------------------------------")
    lista = [] #lista vazia, só aloquei mémoria

    #Agora colocamos um laço de repetição para ficar adicionando os elementos na lista, pq quero percorre elemento por elemento da lista
    i = 0
    while i < tamanho: #enquanto o i for menor que o tamanho(contador/quantas vezes for repetir o código)
        num = int(input("Número: "))
        lista.append(num)
        i += 1 # para não ter o loop infinito
    return lista # retorno a lista para quem quiser utulizar ela depois


#Para pode ver o que está acontecendo na nossa lista, para vermos se está alocando meémoria como deveria
def imprimir_lista(lista): # Lista que foi criado em outra função, está vindo de outra área do programa, por isso devemos usar parâmetros
    print("**- Imprimindo a LISTA -**")
    print("-----------------------------")

    #Pegar a lista e imprimir um por um, por isso iremos usar o for
    for n in lista: #para número em lista
        print(f"Eleemnto: {n}") #estou abrindo objeto(descapitulando)


#Função que vai somar todos os números da lista, e a idade média
def somatorio(lista): #pq não sabemos a lista antes 
    print("**- Somatório dos elementos da LISTA -**")
    print("-------------------------------------------")
    soma = 0 #variavel acumuladora
    for n in lista: #para cada elemento para a minha lista, quero que ele acumule o n 
        soma += n #acumular todos os valores da lista
    return soma


#criar uma função para verificar o número de ocorrências de um determinado número na lista
def verificar_ocorrencias(n ,lista): #verificar se um determinado número está contido na lista, e quantas vezes aparece, passar o número que quero verificar e a lista; N qualquer número
    print("**- Verificar Ocorrências -**")
    print("--------------------------------------------")
    cont = 0 #contadora
    for i in lista: #percorrer a lista um por um, para cada elemento na minha lista, vou verificar se o número i é igual a n
        if i == n: 
            cont += 1
    return cont 
#Quando pede o n dentro do main é melhor, porém quando usamos dentro da def para pedir o n não input é pior, pq está acoplado e pode vir de qualquer lugar
#Pode também criar uma função para pedir o número do usuário também


#criar uma função que retorno uma lista com os valores negativos presentes em uma lista de números inteiros
def separar_negativos(lista):  #tenho que ter uma fonte de dados, que seria a lista
    print("**- Separar elementos negativos -**")
    print("-------------------------------------")
    lista_negativa = []
    for n in lista:
        if n < 0:
            lista_negativa.append(n)
    return lista_negativa




def main():
    t = tamanho_lista() #chamando a função , ela retorna um número inteiro, só estou executando a função tamanho, guardo neste T pq é nele que estamos guardando o tamanho que retornamos
    lista = criar_lista(t) #se retorna em uma lista essa função precisamos guardar em uma váriavel para poder funcionar "lista" 
    imprimir_lista(lista)
    print(f"Soma: {somatorio(lista)}") #pode fazer desse jeito também 
    """somatorio(lista)""" #ela já é reconhecido na main então não precisamos colocar a lista em uma variável
    n = int(input("Digite um número: "))
    verificar_ocorrencias(n, lista) # não temos o parâmetro n, por isso criamos "n = int(input("Digite um número: "))"
    """print(f"Ocorrências de {n} na lista: {verificar_ocorrencias(n, lista)}")""" #também podemos fazer desse jeito
    print(f"Negativos: {separar_negativos(lista)}")
    
    
    


#Principal
main()


