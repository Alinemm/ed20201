#ExE
# #Crie um programa no qual o usuário digitará 5 nomes.
#  Todos os cinco nomes serão salvos no vetor chamado "registros”. Em seguida:
# #Mostre o que o usuário digitou na tela;#O programa pedirá outro nome, 
# que será adicionado no fim do vetor "registros”;
# #O programa pedirá outro nome, que será adicionado na 2ª posição do vetor "registros”;
# #Imprima o resultado na tela.
# 
def main():    
    registros = []    
    for i in range(0,5):        
        nome = input("nome "+str(i+1)+ ": ")       
        registros.append(nome)    
    
    print("lista original: ", registros)    
    registros.append("Aline")    
    
    print("lista modificada 1: ", registros)    
    registros.insert(1, "Morais")    
    print("lista modificada 2: ", registros)

main()