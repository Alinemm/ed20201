#exA
def main():
  dicionario ={}

  print(dicionario)

  for i in range(6):
    chave = input("Qual é o seu nome? ")
    dataNasc = input("Qual é a sua data de nascimento? ")
    dicionario[chave] = dataNasc

  print(dicionario)

main()
