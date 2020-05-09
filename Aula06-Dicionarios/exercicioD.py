#exD
#Crie um dicionário com 6 códigos de barra e o seu respectivo produto e preço.
#Em seguida, remova 2 registros do dicionário por chave e outros 2 registros do dicionário por valores.

estoque = {}
for i in range(3):
  estoque[input("código de barra: ")] = input('produto: ')

codBarra =  input('qual código de barra remover? ')

print ('ANTES:\n', estoque)

estoque[codBarra]=None
#estoque[codBarra].pop()
print ('Remoção do conteúdo de Barra:\n',estoque)

estoque.pop(codBarra)
print ('Remoção do código de Barra:\n', estoque)


