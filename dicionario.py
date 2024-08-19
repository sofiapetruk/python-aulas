#como criar um dicionário 
dicionario = {'chave' : 'valor'}
#print(dicionario)


#dicionario com construtor: 
dicionario = {'primeiro' : 1, 'segundo' : 2, 'terceiro' : 3}
#quando for de outros arquivos de banco de dados você precsar usar o dict para ele separar o que é chave do dicionario
dic_1 = dict(primeiro = 1, segundo = 2, terceiro = 3)


#função zip() - concatenar a chave e o valor, quando quero colocar duas listas em um mesmo dicionario
dic_2 = zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3]) #aqui temos duas listas separado pelo [], precisamos de um construtor para tranformar para dicionario por isso temos que fazer o casting


#casting para dicionario
dic_2 = dict(zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3]))
print(dic_2)

#diconario de uma lista de tuplas
#criar uma tupla - tuplas é igual uma lista que só pode ser de um tamanho único não pode ser adicionado elemento e nada, uma coisa fixa você consegue mexer naquilo mas não na estrutura, tipo o rilho que vem do computador
tupla1 = ('primeiro', 1)
tupla2 = ('segundo', 2)
tuplas3 = ('terceiro', 3) 

#Jogar uma lista de tuplas
lista = [tupla1, tupla2, tuplas3] #lista de objetos

#transformar para o dicionario -- tem que fazer o casting com o construtor
dic_3 = dict(lista)
print(dic_3)

pessoa = {'nome' : 'Pedro', 'idade' : 25, 'altura' : 1.75}
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa.get('nome'))
print(pessoa.get('peso', 'chave não encontrada'))

computador = {'CPU': 'intel', 'RAM': '16gb', 'SSD' : '256'}
#quero pegar o método, utilizo o método quando quero pegar o objeto
print(computador.keys())
print(computador.values())


notas = {'Python': 8, 'Java': 5, 'BD' : 9.5}
print(notas)
print(notas.keys())
print(notas.values())

#Percorrendo um dicionario com for, pq quero pegar elemento por elemento
for chave in notas.keys():
    print(f'Chaves: {chave} e valor: {notas[chave]}') #índice da lista é o chave, como jápegamos a chave no laço 

for nota in notas.values ():
    print(f'Nota: {nota}')

#método items() #pegar os intens se precisar percorrer o laço de repitição
print(notas.items())