#ExG
#Crie um array que o conteúdo seja nomes das cores. Em seguida remova apenas a cor "vermelho”, 
# se houver.

def main():
    cores = ["azul", "amarelo", "verde", "vermelho"]
    if(cores.__contains__("vermelho")):
        cores.remove("vermelho")
        print(cores)
    else:
        cores.clear()
        print(cores)

main()