def forma1():
	area = float(input("Qual o tamanho em metros quadrados da área a ser pintada? "))

	litrosUsados = area/3

	if litrosUsados == int( litrosUsados ):
		custo = litrosUsados * 80
	else:
    		custo = (int(litrosUsados)+1) * 80
	
	print("Custará R$", float("{0:.2f}".format(custo)), " reais")


def forma2():
	areaTotal = float(input("Qual é a área da parede (m2): "))
	numLitros = areaTotal/3
	numLatas  = numLitros/18

	if (int(numLatas) == float(numLatas)):
		print('número de Latas: ', int(numLatas))
		print('preço: ', float(numLatas*80))
	else:
		print('número de Latas: ', int(numLatas+1))
		print('preço: ', float((numLatas+1)*80))

def main():
	forma1()
	forma2()
