#exC
def main():
  locais =  {}

  locais['34242'] = ['Rua das Flores']
  locais['12343'] = ['Rua dos nerds']
  locais['5433'] = ['Rua dos jogadores']
  locais['87686'] = ['Rua dos cataventos']

  #for i in locais.keys():
  #  print (i)

  if '123143' in locais.keys():
    print("Esse CEP já está cadastrado!")
  else:
    print("Esse CEP NÃO está cadastrado!")

  for i in locais.values():
    if 'Rua dos cataventos' in i:
      print("Esse endereço já está cadastrado!")
      

main()
