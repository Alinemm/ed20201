#ExH
#Crie um array referente aos anos de nascimento das 5 pessoas mais próximas a você. 
# Em seguida:
#Ordene o array  na ordem crescente e mostre o resultado;
#Ordene o array na ordem decrescente e mostre o resultado;

def main():
    anosNasc = input("Digite os anos de nascimento de 5 pessoas próximas a você: ").split(" ")
    print(anosNasc)
    anosNasc.sort()
    print(anosNasc)
    anosNasc.sort(reverse=True)
    print(anosNasc)

main()