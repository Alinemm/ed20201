#exD
def main():
  m = [[1,2,3,4],[5,6,7,8]]

  #novoValor =  int(input("Novo valor: "))

  print(m)
  for linha in m:
    #novoValor =  int(input("Novo valor: "))
    linha.append(int(input("Novo valor: ")))

  print(m)


main()