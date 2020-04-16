#exF
def main():
  cadastro = []

  for i in range(0,3):
    linha = input("Digite nome, matricula e data de nascimento, separados por vírgula: ").split(",")
    cadastro.append(linha)
  print(cadastro)
    
'''
  for i in range(0,3):
    linha = []
    for j in range(0,1):
      nome = input("Nome: ")
      matrícula = input("Matrícula: ")
      dataNasc = input("Data de Nascimento: ")
      linha.append(nome)
      linha.append(matrícula)
      linha.append(dataNasc)
    cadastro.append(linha)
 ''' 
  

main()