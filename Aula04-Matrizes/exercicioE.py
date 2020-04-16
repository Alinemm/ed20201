#exEdef main():
  matriz = []

  tam = int(input('Qual é o tamanho da sua matriz quadrada? (número)'))

  for linha in range(0,tam):
    vetorLinha = []
    for coluna in range (0,tam):
      valor = int(input("Valor a["+str(linha+1)+","+str(coluna+1)+ "]:"))
      vetorLinha.append(valor)
    matriz.append(vetorLinha)

  print(matriz)
  contador = 0
  for linha in matriz:
    for valor in linha:
      #print(linha)
      if valor > 10:
        contador = contador + 1

  print("A matriz tem ", contador, "elemento(s) maior(es) do que 10!")

main()