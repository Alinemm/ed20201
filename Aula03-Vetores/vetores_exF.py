#ExF
#Crie um programa no qual o usuário digitará 5 nomes num vetor (OBRIGATÓRIO TER SEU NOME INCLUÍDO NO VETOR). Em seguida:
#a) mostre os valores na tela.
#b) adicione seu sobrenome na posição do seu nome no array.
#c) imprima o resultado na tela.

def main():
    lista = []
    for i in range(0,5):
        nome = input("nome "+str(i+1)+ ": ")
        lista.append(nome)
    print("lista original: ", lista)

    pos = lista.index("Aline")
    print(pos)

    lista.insert(pos, "Morais")
    print("lista modificada 2: ", lista)

main()

