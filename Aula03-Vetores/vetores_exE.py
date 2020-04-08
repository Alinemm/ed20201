#ExE
#Crie um programa no qual o usuário digitará 5 nomes. Todos os cinco nomes serão salvos no vetor chamado "registros”. Em seguida:
#Mostre o que o usuário digitou na tela;
#O programa pedirá outro nome, que será adicionado no fim do vetor "registros”;
#O programa pedirá outro nome, que será adicionado na 2ª posição do vetor "registros”;
#Imprima o resultado na tela.

def main():
    lista = []
    for i in range(0,5):
        nome = input("nome "+str(i+1)+ ": ")
        lista.append(nome)
    print("lista original: ", lista)

    lista.append("Aline")
    print("lista modificada 1: ", lista)
    lista.insert(1, "Morais")
    print("lista modificada 2: ", lista)

main()

