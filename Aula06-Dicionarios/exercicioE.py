#exE
#Crie um dicionário que armazene informações sobre nome, endereço e cpf de 3 usuários. Em seguida, mostre na tela.
#OBS: as chaves dos usuário devem ter os mesmos nomes entre si (nome, endereço e cpf).


dicts = []
dicionario = {}

for i in range(3):
   dicionario['nome'] = input("nome: ")
   dicionario['cpf'] = input("cpf: ")
   dicionario['endereco'] = input("endereco: ")
   dicts.append(dicionario.copy())

print(dicts)


