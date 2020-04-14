#TED 04

def resultado():
    opcao = input(" ")
    escolha = opcao.split(" ")
    if(escolha[0] == "tesoura"):
        if(escolha[1] == "papel" or escolha[1] == "lagarto"):
            print("Bazinga!!")
        elif(escolha[1] == "tesoura"):
            print("De novo!!!")
        else:
            print("Raj trapaceou")
    elif(escolha[0] == "papel"):
        if(escolha[1] == "pedra" or escolha[1] == "Spock"):
            print("Bazinga!!")
        elif(escolha[1] == "papel"):
            print("De novo!!!")
        else:
            print("Raj trapaceou")
    elif(escolha[0] == "pedra"):
        if(escolha[1] == "lagarto" or escolha[1] == "tesoura"):
            print("Bazinga!!!")
        elif(escolha[1] == "pedra"):
            print("De novo!!!")
        else:
            print("Raj trapaceou")
    elif(escolha[0] == "lagarto"):
        if(escolha[1] == "Spock" or escolha[1] == "papel"):
            print("Bazinga!!!")
        elif(escolha[1] == "lagarto"):
            print("De novo!!!")
        else:
            print("Raj trapaceou")
    elif(escolha[0] == "Spock"):
        if(escolha[1] == "tesoura" or escolha[1] == "pedra"):
            print("Bazinga!!!")
        elif (escolha[1] == "Spock"):
            print("De novo!!!")
        else:
            print("Raj trapaceou")

def main():
    rodadas = int(input("Informe o numero de rodadas maior que zero "))
    if rodadas != 0:
        i = 0
        while i < rodadas:
            print("Caso#", i+1, end=" ")
            resultado()
            i = i + 1
    print("Numero de rodadas igual ou menor que zero")
main()