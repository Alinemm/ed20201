def calc1(n1T, n2T):
  conta = (2*n1T) * (n2T/2)
  return conta

def calc2(n1T,n3T):
  return ((3*n1T)+(n3T))

def calc3(n3T):
  return (n3T ** 3)


def main():
  n1 = int(input("Digite o núúmero 1: "))
  n2 = int(input("Digite o núúmero 2: "))
  n3 = float(input("Digite o núúmero 3: "))

  print('Calc 1:',calc1(n1,n2))
  print('Calc 2:',calc2(n1, n3))
  print('Calc 3:',calc3(n3))

main()
