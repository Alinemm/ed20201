#ExC
#Crie um programa que o usuário digite uma sequência de valores (de tamanho dinâmico) numa única variável, chamada registro. Em seguida, mostre os valores armazenados.
def solucao1():
    registro = [45,86]

    tamanho = int(input("Quantos elementos a inserir? "))

    for i in range(0,tamanho):
        tmp = input("Valor "+ str(i)+ ": ")
        registro.append(tmp)

    print(registro)

def solucao2():
    registro = input("Digite os valores, separados por vírgula: ").split(",")
    print(registro)


solucao1()
solucao2()