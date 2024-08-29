#DICIONARIO

#dicionario vazio
dicionario = {}

#dicionario com itens
dicionario = {'name': 'Thiago',
              'idade': 18,
              "profissao" : 'softwareEngineer'}
print(dicionario)

#acessar um item
print(dicionario['profissao'])

#altera um item
dicionario['idade'] = 19
print(dicionario)

#inserir novo item
dicionario['email'] = 'thiago@email.com'
print(dicionario)

#remover um item
dicionario.pop('email')
print(dicionario)

#preencher um dicionario para castro de aluos
alunos = {}
while True:
    rm = input ('RM: ')
    if rm == '':
        break
    nome = input('Nome: ')
    if rm not in alunos:
        alunos[rm] = nome
    else:
        print('O rm ja foi cadastrado')
    alunos[rm] = nome
print(alunos)

#percorrer as chaves
for chave in dicionario.keys():
    print(chave)

#percorrer os valores
for valor in dicionario.values():
    print(valor)

#percorrer os itens
for chave, valor in dicionario.items():
    print(chave, valor)

#dicionario armazenando listas
notas = {'rm1234':[7,8,9,0], 'rm4567': [6,8.5,10], 'rm2222':[5,9,10]}
print(notas['rm1234'][2])
notas['rm2222'][0] = 7.75
print(notas)

#dicionario de dicionarios
# Dicionário de dicionários
alunos = {
    'rm1234': {'nome': 'Ana', 'Turma': '1ESPG', 'notas': [10, 10, 9]},
    'rm8766': {'nome': 'Thiago', 'Turma': '1ESPG', 'notas': [10, 10, 10]}
}

# Correção no acesso às chaves
print(alunos['rm8766']['Turma'])  # Note o 'T' maiúsculo
print(alunos['rm8766']['notas'])
