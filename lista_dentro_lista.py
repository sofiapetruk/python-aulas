#criar uma função que irá mapear a nota de um aluno em uma lista
def coletar_nota():
    notas = input().split() #split , o usuario coloca as notas de uma fez só, sem precisar usar o while; #não sabemos quantas notas eu quero por padrão ele é String
    for i in range(len(notas)): #percorre essa lista elemento por elemento e depois converter para número, já quele ele está como uma String
        notas[i] = float(notas[i])   #fazer o casting, o que é? converter String para float, 
    return notas


#função para preencher a turma, tem que saber quantos alunos tem nesssa turm
def preencher_turma(qtde_alunos): # é terminante pq quantos alunos tiver terá que roda o coletar_nota tanta vezes
    turma = []
    for i in range(qtde_alunos):
        print(f"{i+1} aluno: ", end=" ")
        aluno = coletar_nota()
        turma.append(aluno) #sequência atras de sequência, lista dentro de lista
    return turma


#criar uma função para calcular a média de um aluno
"""def media_aluno(turma, notas):
    soma = 0
    for aluno in range(len(turma)):
        turma[aluno] = coletar_nota()
        soma += notas
        media = soma / (len(notas))
        print(f"A média do primeiro aluno é: {media}")
    return media""" #jeito errado

def calculo_media(notas): # refeito pelo o que o professor explicou
    soma = 0
    for aluno in notas:
        soma += aluno
    return soma / len(notas)

"""def calcular_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
    return soma / len(aluno)""" #jeito do professor


#notas dos alunos e quais são as médias
def resumo_turma(turma): #imprimir aluno, nota e média
    for aluno in turma:    #manipular lista de lista, tenho que chegar no nível de turma; PARA CADA ALUNO EM TURMA, VAI SÓ UM ALUNO POR VEZ PQ ESTÁ PERCORRENDO ELEMENTO POR ELEMENTO
        media = calculo_media(aluno)
        print(f"Notas: {aluno} --- Média: {media:.2f}") #só estou pegando a nota daquele aluno; É VOID NÃO RETORNA NADA


#Principal
#notas = coletar_nota()
qtd_alunos = int(input("Quantidade: "))
turma = preencher_turma(qtd_alunos)
resumo_turma(turma)