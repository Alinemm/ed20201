#TED 03
# Crie uma agenda eletrônica que contenha dois vetores: um array com o nome dos seus amigos e outro com as suas
# respectivas datas de aniversário.
# Tente inserir e remover as informações da agenda de maneira dinâmica (apagando pelo nome ou posição,
# inserindo n usuários por vez caso queira, etc...).

def imprimirAgenda(nomes, datasAniversario):
    print()
    if len(nomes) == 0 and len(datasAniversario) == 0:
        print("Não há elementos para imprimir")
    else:
        i = 1
        for (x,y) in zip(nomes, datasAniversario):
            print(i,"º - Nome:", x, ", Data Aniversário:", y)
            i = i + 1

def inserirContato(nomes, datasAniversario):
    qnt = int(input("Quantos contatos deseja inserir"))
    if qnt != 0:
        i = 0
        while i < qnt:
            nome = input("Nome do contato")
            data = input("Data de aniversário")
            nomes.append(nome)
            datasAniversario.append(data)
            i = i + 1
    else:
        return 0

def removeContato(nomes, datasAniversario):
    if len(nomes) == 0 and len(datasAniversario) == 0:
        print("Não há o que remover")
        return 0
    else:
        print("1- Remover pelo nome")
        print("2- Remover pela posição")
        opcao = input("_")
        if opcao == "1":
            nome=input("informe o nome")
            pos = nomes.index(nome)
            del nomes[pos]
            del datasAniversario[pos]
        elif opcao == "2":
            pos = int(input("informe a posição"))
            del nomes[pos-1]
            del datasAniversario[pos-1]

def menu(nomes, datasAniversario):
    print("Bem vindo a minha agenda")
    print("1- inserir contatos na agenda")
    print("2- remover contatos na agenda")
    print("3- imprimir agenda")
    print("0- encerrar agenda")
    opcao = input("_")
    if opcao == "1":
        if inserirContato(nomes, datasAniversario) != 0:
            print("Contato inserido com sucesso!!")
        else:
            print("Erro ao inserir contato, quantidade inválida")
    elif opcao == "2":
        if removeContato(nomes,datasAniversario) != 0:
            print("Contato removido com sucesso!!")
        else:
            print("Erro ao remover contato")
    elif opcao == "3":
        imprimirAgenda(nomes, datasAniversario)
    elif opcao == "0":
        return 0

def main():
    nomes = []
    datasAniversario = []

    while True:
        if menu(nomes,datasAniversario) != 0:
            print()
        else:
            break


main()